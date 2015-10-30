# -*- coding:utf-8 -*-

from .form import *
from .models import *

from django.template.context_processors import csrf
from django.template import RequestContext
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.core.urlresolvers import reverse
from django.core.files import File
from django.contrib.syndication.views import Feed
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class RSSFeed(Feed):
	title = 'RSS feed -article'
	link = 'feeds/posts/'
	description = 'RSS feed - job posts'
	def items(self):
		return Job.objects.order_by('-create_date')
	def item_title(self,item):
		return item.name
	def item_pubdate(self,item):
		return item.create_date
	def item_description(self,item):
		return item.technique
#	def item_link(self,item):
#		return reverse('job',args=[item.pk])

def log(req):
	if req.method == "POST":
		if req.POST.has_key('person_login'):
			person_login_form = PersonLoginForm(req.POST)
			if person_login_form.is_valid():
				account = person_login_form.cleaned_data['account']
				password = person_login_form.cleaned_data['password']
				person = Person.objects.filter(account__exact=account,password__exact=password)
				if person:
					person = person[0]
					#response = HttpResponseRedirect('home')
					response = HttpResponseRedirect(reverse('home'))
					response.set_cookie('person_id',person.id,3600)
					response.set_cookie('person_name',person.true_name,3600)
					response.delete_cookie('company_id')
					response.delete_cookie('company_name')
					return response
		elif req.POST.has_key('person_logup'):
			person_logup_form = PersonLogupForm(req.POST)
			if person_logup_form.is_valid():
				account = person_logup_form.cleaned_data['account']
				name = person_logup_form.cleaned_data['true_name']
				password = person_logup_form.cleaned_data['password']
				person = Person.objects.filter(account__exact=account)
				if person:
					person = Person.objects.create(account=account,true_name=name,password=password)
					response = HttpResponseRedirect(reverse('home'))
					response.set_cookie('person_id',person.id,3600)
					response.set_cookie('person_name',person.true_name,3600)
					response.delete_cookie('company_id')
					response.delete_cookie('company_name')
					return response
		elif req.POST.has_key('company_login'):
			company_login_form = CompanyLoginForm(req.POST)
			if company_login_form.is_valid():
				account = company_login_form.cleaned_data['account']
				password = company_login_form.cleaned_data['password']
				company = Company.objects.filter(account__exact=account,password__exact=password)
				if company:
					company = company[0]
					response = HttpResponseRedirect(reverse('home'))
					response.set_cookie('company_id',company.id,3600)
					response.set_cookie('company_name',company.name,3600)
					response.delete_cookie('person_id')
					response.delete_cookie('person_name')
					return response
		elif req.POST.has_key('company_logup'): 
			company_logup_form = CompanyLogupForm(req.POST)
			if company_logup_form.is_valid():
				account = company_logup_form.cleaned_data['account']
				name = company_logup_form.cleaned_data['name']
				password = company_logup_form.cleaned_data['password']
				company = Company.objects.filter(account__exact=account)
				if company:
					company = Company.objects.create(account=account,name=name,password=password)
					response = HttpResponseRedirect(reverse('home'))
					response.set_cookie('company_id',company.id,3600)
					response.set_cookie('company_name',company.name,3600)
					response.delete_cookie('person_id')
					response.delete_cookie('person_name')
					return response
		#  or 	if person_login_form not in locals().keys():
		if 'person_login_form' not in dir():
			person_login_form = PersonLoginForm()
		if 'person_logup_form' not in dir():
			person_logup_form = PersonLogupForm()
		if 'company_login_form' not in dir():
			company_login_form = CompanyLoginForm()
		if 'company_logup_form' not in dir():
			company_logup_form = CompanyLogupForm()
	else:
		person_login_form = PersonLoginForm()
		person_logup_form = PersonLogupForm()
		company_login_form = CompanyLoginForm()
		company_logup_form = CompanyLogupForm()
	username = req.COOKIES.get('company_name',None)
	if not username:
		username = req.COOKIES.get('person_name',None)
	return render(req,'log.html',locals())
def logout(req):
	response = HttpResponseRedirect(reverse('home'))
	response.delete_cookie('person_id')
	response.delete_cookie('person_name')
	response.delete_cookie('company_id')
	response.delete_cookie('company_name')
	return response



def job(req,id):
	job = Job.objects.filter(id=id)[0]
	person_name = req.COOKIES.get('person_name',None)
	if person_name:
		person_id = req.COOKIES.get('person_id')
		person = Person.objects.get(id=person_id)
		collected = person.collection.filter(id=id)
		applied = person.app_record.filter(id=id)
	company_name = req.COOKIES.get('company_name',None)
	return render(req,'job.html',locals())

def cv(req,id):
	cv = CV.objects.filter(id=id)[0]
	person_name = req.COOKIES.get('person_name',None)
	company_name = req.COOKIES.get('company_name',None)
	return render(req,'cv.html',locals())


# person user views
def get_person(func):
	def view(req,*args,**kw):
		id = req.COOKIES.get('person_id',None)
		if id:	
			person = Person.objects.filter(id__exact=id)[0]
			return func(req,person,*args,**kw)
		else:
			return HttpResponseRedirect(reverse('home'))
	return view

def person(req,person):
	person_name = person.true_name	
	return render(req,'person.html',locals())

def person_change(req,person):
	person_name = person.true_name	
	if req.method == 'GET':
		person_basic_form = PersonBasicForm(instance=person)
		return render(req,'person_form.html',locals())
	elif req.method == 'POST':
		#old_avatar = person.avatar
		#person_basic_form = PersonBasicForm(req.POST,req.FILES,instance=person)
		#person_basic_form.save()
		#if old_avatar.name != person.avatar.name:
		#	old_avatar.delete()
		#print(old_avatarperson.avatar,person.true_name,person.email,person.phone,person.city,person.school)
		person_basic_form = PersonBasicForm(req.POST,req.FILES,instance=person)
		if person_basic_form.is_valid():
			if person_basic_form.files.get('avatar',None):
				avatar = person_basic_form.files['avatar']
				django_file = File(avatar)
				person.avatar.delete()
				person.avatar.save('static/upload/avatar/'+django_file.name,django_file,save=False)
		person.save()
		return HttpResponseRedirect(reverse('person'))
	
def cv_add(req,person):
	person_name = person.true_name	
	if req.method == 'POST':
		cv = CV()
		cv_form = CVForm(req.POST,instance=cv)
		if cv_form.is_valid():
			cv.person = person
			cv.save()
			return HttpResponseRedirect(reverse('cv',kwargs={'id':cv.id}))
	else:
		cv_form = CVForm()
	submit = '添加'
	return render(req,'cv_form.html',locals())

def cv_delete(req,person,id):
	cv = CV.objects.filter(id=id)
	if cv:
		cv[0].delete()
	return HttpResponseRedirect(reverse('person'))

def cv_change(req,person,id):
	person_name = person.true_name	
	if req.method == 'GET':
		cv = CV.objects.filter(id=id)[0]
		cv_form = CVForm(instance=cv)
		submit = '修改'
		return render(req,'cv_form.html',locals())
	elif req.method == 'POST':
		cv = CV.objects.filter(id=id)[0]
		cv_form = CVForm(req.POST,instance=cv)
		if cv_form.is_valid():
			cv.save()
		return HttpResponseRedirect(reverse('cv',kwargs={'id':cv.id}))

def job_collect(req,person,id):
	job = Job.objects.filter(id=id)
	if job:
		job = job[0]
		person.collection.add(job)
		return HttpResponse('ok')
	else:
		return HttpResponse('wrong job id')
	
def job_apply(req,person,id):
	job = Job.objects.filter(id=id)
	if job:
		job = job[0]
		progress = App_progress(person=person,job=job)
		person.app_progress_set.add(progress)
		return HttpResponse('ok')
	else:
		return HttpResponse('wrong job id')
	


# company user views
def get_company(func):
	def view(req,*args,**kw):
		id = req.COOKIES.get('company_id',None)
		if id:	
			company = Company.objects.filter(id__exact=id)[0]
			return func(req,company,*args,**kw)
		else:
			return HttpResponseRedirect(reverse('home'))
	return view

def company(req,company):
	company_name = company.name
	return render(req,'company.html',locals())
		
def company_change(req,company):
	company_name = company.name
	if req.method == 'GET':
		company_form = CompanyForm(instance=company)
		return render(req,'company_form.html',locals())
	elif req.method == 'POST':
		company_form = CompanyForm(req.POST,instance=company)
		if company_form.is_valid():
			company.save()
		return HttpResponseRedirect(reverse('company'))
	return render(req,'company_form.html',locals())

def job_add(req,company):
	company_name = company.name
	if req.method == 'POST':
		job = Job()
		job_form = JobForm(req.POST,instance=job)
		if job_form.is_valid():
			job.company = company
			job.save()		# 必须在m2m之前
			tag = Tag.objects.filter(id=int(req.REQUEST['tags']))
			if tag:
				tag = tag[0]
				job.tags.add(tag)
			welfare = Welfare.objects.filter(id=int(req.REQUEST['welfares']))
			if welfare:
				welfare = welfare[0]
				job.welfares.add(welfare)
			return HttpResponseRedirect(reverse('job',kwargs={'id':job.id}))
	else:
		job_form = JobForm()
	submit = '添加'
	return render(req,'job_form.html',locals())

def job_delete(req,company,id):
	job = Job.objects.filter(id=id)
	if job:
		job[0].delete()
	return HttpResponseRedirect(reverse('company'))

def job_change(req,company,id):
	if req.method == 'POST':
		job = Job.objects.filter(id=id)
		if job:
			job = job[0]
			job_form = JobForm(req.POST,instance=job)
			if job_form.is_valid():
				job.save()
				# fix it   form can check changes
				job.welfares.clear()
				job.tags.clear()
				tag = Tag.objects.filter(id=int(req.REQUEST['tags']))
				if tag:
					tag = tag[0]
					job.tags.add(tag)
				welfare = Welfare.objects.filter(id=int(req.REQUEST['welfares']))
				if welfare:
					welfare = welfare[0]
					job.welfares.add(welfare)
				return HttpResponseRedirect(reverse('job',kwargs={'id':job.id}))
	else:
		job = Job.objects.filter(id=id)
		if job:
			job = job[0]
		job_form = JobForm(instance=job)
	submit = '修改'
	return render(req,'job_form.html',locals())
def home(req):
	person_name = req.COOKIES.get('person_name',None)
	if not person_name:
		company_name = req.COOKIES.get('company_name',None)

	if req.GET.has_key('job_key'):
		print('job')
		key = req.GET['job_key']
		alljob = Job.objects.filter(name__icontains=key)
		paginator = Paginator(alljob,8)
		page = req.GET.get('page')
		try:
			joblist = paginator.page(page)
		except PageNotAnInteger:
			joblist = paginator.page(1)
		except EmptyPage:
			joblist = paginator.page(paginator.num_pages)
		return render(req,'job_search.html',locals())
	elif req.GET.has_key('company_key'):
		print('company')
		key = req.GET['company_key']
		companylist = Company.objects.filter(name__icontains=key)
		return render(req,'company_search.html',locals())
	else:
		print('home')
		return render(req,'home.html',locals())











def test(req,num):
	if num == '1':
		return render(req,'test1.html')
	if num == '2':
		return render(req,'test2.html')
	if num == '3':
		return render(req,'test3.html')
def test1(req):
	return render(req,'test1.html')
def test2(req):
	return render(req,'test2.html')
def test3(req):
	return render(req,'test3.html')
def get_test(func):
	def view(req):
		print(func.func_name)
		return func(req)
	return view
