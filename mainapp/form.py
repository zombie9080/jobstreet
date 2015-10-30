from .models import *
from django.forms import ModelForm  
from django import forms

class PersonLoginForm(ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = Person
		fields = ['account','password']
	#account = forms.CharField()
	#password = forms.CharField(widget=forms.PasswordInput)

class PersonLogupForm(ModelForm):
	class Meta:
		model = Person
		fields = ['account','true_name','password']
		widgets = {
			'password': forms.PasswordInput(),
		}
	#account = forms.CharField()
	#name = forms.CharField()
	#password = forms.CharField(widget=forms.PasswordInput)

class PersonBasicForm(ModelForm):
	class Meta:
		model = Person
		fields = ['true_name','email','phone','city','school']
	

class CVForm(ModelForm):
	class Meta:
		model = CV
		fields = ['name','expected_salary','job_objective','technique','experience','evaluation']

class CompanyLoginForm(ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = Company
		fields = ['account','password']
	#account = forms.CharField()
	#password = forms.CharField(widget=forms.PasswordInput)

class CompanyLogupForm(ModelForm):
	class Meta:
		model = Company
		fields = ['account','name','password']
		widgets = {
			'password': forms.PasswordInput(),			
		}
	#account = forms.CharField()
	#name = forms.CharField()
	#password = forms.CharField(widget=forms.PasswordInput)
class CompanyForm(ModelForm):
	class Meta:
		model = Company
		fields = ['name','scale','city','address','summary']

class JobForm(ModelForm):
	tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),to_field_name='id')
	welfares = forms.ModelMultipleChoiceField(queryset=Welfare.objects.all(),to_field_name='id')
	class Meta:
		model = Job
		fields = ['name','salary','count','years','tags','welfares','attach_welfare','technique','duty']
