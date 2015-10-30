
# !-- coding=utf8 --#

from django.db import models
from django.core.urlresolvers import reverse

CITY = ( ('bj','北京'),('sh','上海'),('gz','广州'),('SZ','深圳'),('wh','武汉'),('xa','西安'),('hz','杭州'),('nj','南京'),('cd','成都'),('cq','重庆'),('dw','东莞'),('dl','大连'),('sy','沈阳'),('sz','苏州'),('km','昆明'),('cs','长沙'),('hf','合肥'),('lb','宁波'),('zz','郑州'),('tj','天津'),('qd','青岛'),('jn','济南'),('heb','哈尔滨'),('cc','长春'),('fz','福州'),)
SALARY = (('0','面议'),('1','2000-2999'),('2','3000-4499'),('3','4500-5999'),('4','6000-7999'),('5','8000-9999'),('6','10000-14999'),('7','15000-19999'),('8','20000-24999'),('9','25000-29999'),('10','30000-39999'),('11','40000-49999'),('12','50000-69999'),('13','70000-99999'),('14','100000以上'),)
	#AREA = ()
class Person(models.Model):
	#CITY = ( ('bj','北京'),('sh','上海'),('gz','广州'),('sz','深圳'),('wh','武汉'),('xa','西安'),('hz','杭州'),('nj','南京'),('cd','成都'),('cq','重庆'),('dw','东莞'),('dl','大连'),('sy','沈阳'),('sz','苏州'),('km','昆明'),('cs','长沙'),('hf','合肥'),('lb','宁波'),('zz','郑州'),('tj','天津'),('qd','青岛'),('jn','济南'),('heb','哈尔滨'),('cc','长春'),('fz','福州'),)
	account = models.CharField(max_length=50)
	password = models.CharField(max_length = 30)
	true_name = models.CharField(max_length=20)
	email = models.EmailField()
	phone = models.CharField(max_length=11)
	avatar = models.ImageField(upload_to='static/upload/avatar')
	city = models.CharField(max_length=3,choices=CITY)
	school = models.CharField(max_length=40)
#	collection = models.ManyToManyField('Job',related_name='+',null=True,blank=True)
	collection = models.ManyToManyField('Job',related_name='+')
	app_record = models.ManyToManyField('Job',through='App_progress',through_fields=('person','job'))
	def __unicode__(self):
		return self.true_name
	class Meta:
		ordering = ['city']

class App_progress(models.Model):
	STATUS = (
		('ap','Applicated'),	
		('sc','Scanned'),
		('in','Interview'),
		('of','Offer'),
	)
	person = models.ForeignKey('Person')
	job = models.ForeignKey('Job')
	progress = models.CharField(max_length=2,choices=STATUS,default='ap')
	def __unicode__(self):
		return self.get_progress_display()

class CV(models.Model):
	name = models.CharField(max_length=30)
	expected_salary = models.CharField(max_length=2,choices=SALARY)
	job_objective = models.CharField(max_length=100)
	technique = models.TextField()
	experience = models.TextField()
	evaluation = models.TextField()
	person = models.ForeignKey(Person)
	def __unicode__(self):
		return self.name
	class Meta:
		ordering = ['person']

class Tag(models.Model):
	name = models.CharField(max_length=10)

	def __unicode__(self):
		return self.name

class Welfare(models.Model):
	name = models.CharField(max_length=20)
	def __unicode__(self):
		return self.name

class Job(models.Model):
	WORK_YEARS = (('0','应届毕业生'),('1','1~2年'),('2','3~4年'),('3','5年以上'),)
	name = models.CharField(max_length=30)
	years = models.CharField(max_length=1,choices=WORK_YEARS)
	salary = models.CharField(max_length=2,choices=SALARY,blank=True,null=True)
	welfares = models.ManyToManyField('Welfare')
	attach_welfare = models.TextField(blank=True,null=True)
	tags = models.ManyToManyField('Tag')
	count = models.IntegerField(default=1)
	technique = models.TextField()
	duty = models.TextField()
	create_date = models.DateTimeField(auto_now=True)
	company = models.ForeignKey('Company')
	def get_absolute_url(self):
		return reverse('job',args=[self.id])
	def __unicode__(self):
		return self.name
	class Meta:
		ordering = ['-create_date']

class Company(models.Model):
	SCALE=(('0','少于50人'),('1','50-150人'),('2','150-500人'),('3','500-1000人'),('4','1000-5000人'),('5','5000-10000人'),('6','10000人以上'),)
	#CITY = ( ('bj','北京'),('sh','上海'),('gz','广州'),('sz','深圳'),('wh','武汉'),('xa','西安'),('hz','杭州'),('nj','南京'),('cd','成都'),('cq','重庆'),('dw','东莞'),('dl','大连'),('sy','沈阳'),('sz','苏州'),('km','昆明'),('cs','长沙'),('hf','合肥'),('lb','宁波'),('zz','郑州'),('tj','天津'),('qd','青岛'),('jn','济南'),('heb','哈尔滨'),('cc','长春'),('fz','福州'),)
	#AREA=()
	account = models.CharField(max_length=50)
	password = models.CharField(max_length=30)
	name = models.CharField(max_length=30,unique=True)
	scale = models.CharField(max_length=1,choices=SCALE)
	city = models.CharField(max_length=2,choices=CITY)
	#area = models.CharField(max_length=1,choices=AREA)
	address = models.CharField(max_length=100)
	summary = models.TextField()
	def __unicode__(self):
		return  self.name
	class Meta:
		ordering = ['city']
