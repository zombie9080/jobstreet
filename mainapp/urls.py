"""jobstreet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from views import *

urlpatterns = [
		url(r'^$',home,name='home'),
		url(r'^log/$',log,name='log'),
		url(r'^logout/$',logout,name='logout'),


		url(r'^job/(?P<id>\d+)/$',job,name='job'),
		url(r'^cv/(?P<id>\d+)/$',cv,name='cv'),
		url(r'^person/(?P<id>\d+)/$',person_view,name='person_view'),
		url(r'^company/(?P<id>\d+)/$',company_view,name='company_view'),
		# person
		url(r'^person/$',get_person(person),name='person'),
		url(r'^person/change/$',get_person(person_change),name='person_change'),
		url(r'^person/cv_add/$',get_person(cv_add),name='cv_add'),
		url(r'^person/cv_delete/(?P<id>\d+)/$',get_person(cv_delete),name='cv_delete'),
		url(r'^person/cv_change/(?P<id>\d+)/$',get_person(cv_change),name='cv_change'),
		url(r'^person/job_apply/(?P<id>\d+)/$',get_person(job_apply),name='job_apply'),
		url(r'^person/job_apply_delete/(?P<id>\d+)/$',get_person(job_apply_delete),name='job_apply_delete'),
		url(r'^person/job_apply_mary/$',get_person(job_apply_mary),name='job_apply_mary'),
		url(r'^person/job_collect_add/(?P<id>\d+)/$',get_person(job_collect_add),name='job_collect_add'),
		url(r'^person/job_collect_add_mary/$',get_person(job_collect_add_mary),name='job_collect_add_mary'),
		url(r'^person/job_collect_delete/(?P<id>\d+)/$',get_person(job_collect_delete),name='job_collect_delete'),
		# company
		url(r'^company/$',get_company(company),name='company'),
		url(r'^company/change/$',get_company(company_change),name='company_change'),
		url(r'^company/job_add/$',get_company(job_add),name='job_add'),
		url(r'^company/job_delete/(?P<id>\d+)/$',get_company(job_delete),name='job_delete'),
		url(r'^company/job_change/(?P<id>\d+)/$',get_company(job_change),name='job_change'),
		url(r'^company/job_app_progress/$',get_company(job_app_progress),name='job_app_progress'),
		#url(r'^company/job_apply_list/(?P<id>\d+)/$',get_company(job_apply_list),name='job_apply_list'),

		url(r'^feed/$',RSSFeed(),name='RSS'),
		#url(r'^test/(\d)/$',test,name='test'),
		url(r'^test/1/$',get_test(test1),name='test1'),
		url(r'^test/2/$',get_test(test2),name='test2'),
		url(r'^test/3/$',get_test(test3),name='test3'),
		url(r'^test/0/$',get_test(test0),name='test0'),
]
