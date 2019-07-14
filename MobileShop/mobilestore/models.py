from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Mobile(models.Model):
	Model_Name          = 	 models.CharField(max_length=50)
	Image		        = 	 models.ImageField(upload_to='mobileImage')
	Brand               =	 models.CharField(max_length=50)
	Price	            =	 models.IntegerField()
	Descrption 			= 	 models.CharField(max_length=150,default="face recognition,13 mp cammera ")

	def __str__(self):
		return self.Model_Name

class Cart(models.Model):
	user 		= models.ForeignKey(User,on_delete=models.CASCADE)
	mobile      = models.ForeignKey(Mobile,on_delete=models.CASCADE)

	def __str__(self):
		return self.mobile.Model_Name	