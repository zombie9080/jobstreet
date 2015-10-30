from django.contrib import admin
from .models import *

class PersonAdmin(admin.ModelAdmin):
	list_display = ('true_name','email','phone','school','city','avatar')
	list_filter = ('city',)
	search_fields = ('city','true_name')

class JobAdmin(admin.ModelAdmin):
	list_display = ('name','salary','years','count','company','create_date')
	list_filter = ('create_date',)
	search_fields = ('name','create_date')
	def company(self):
		return self.company.name

class CompanyAdmin(admin.ModelAdmin):
	list_display = ('name','scale','city','address')
	list_filter = ('name','city')
	search_fields = ('name','city')

class App_progressAdmin(admin.ModelAdmin):
	list_display = ('person','job','progress')
	list_filter = ('person','job')
	search_fields = ('person','job')

admin.site.register(Person,PersonAdmin)
admin.site.register(App_progress,App_progressAdmin)
admin.site.register(CV)
admin.site.register(Job,JobAdmin)
admin.site.register(Tag)
admin.site.register(Welfare)
admin.site.register(Company,CompanyAdmin)


