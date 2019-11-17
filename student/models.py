from django.db import models





class Administration(models.Model):
	name=models.CharField('name', max_length=1000,default='')
	number=models.CharField('administration number',max_length=20,default='')
	adress=models.CharField('Administration adress', max_length=1000,default='')
	owner=models.ForeignKey('auth.User',related_name='owner2', on_delete=models.CASCADE, default='')

	def __str__(self):
		return self.name


class Teachers(models.Model):
	teacher_name=models.CharField('Teacher name', max_length=1000,default='')
	teacher_number=models.CharField('Teacher number',max_length=20,default='')
	teacher_lesson=models.CharField('Teacher lesson', max_length=1000,default='')
	teacher_history=models.TextField('Teacher history',default='')
	owner=models.ForeignKey('auth.User',related_name='owner1', on_delete=models.CASCADE, default='')


	def __str__(self):
		return self.teacher_name

class VUZY(models.Model):
	ch = (
			('1', 'All'),
			('2', 'Medical'),
			('3', 'Gumanytarian'),
			('4',  'STEM'),
		)
	name=models.CharField('University name', max_length=1000,default='')
	about=models.TextField('About University',default='')
	
	region=models.CharField('University region', max_length=100,default='')
	category=models.CharField('University category', max_length=20, choices=ch,default='',)
	ort_porog=models.PositiveIntegerField('Min Ort',default='')
	prize=models.PositiveIntegerField('Study prize(som)',default='')
	examination_examples=models.TextField('Examination examples',default='')
	administration=models.ManyToManyField(Administration)
	teachers=models.ManyToManyField(Teachers)
	'''date=models.DateField('date of delivery',max_length=20,default='')
				date1=models.DateField('Last day of delivery',max_length=1000,default='')'''
	owner=models.ForeignKey('auth.User',related_name='owner', on_delete=models.CASCADE, default='')
	

	def __str__(self):
		return self.name


