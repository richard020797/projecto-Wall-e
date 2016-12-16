from django.db import models
from modules.User.models import User

class Session(models.Model):
	id_session = models.AutoField(primary_key=True)
	title = models.CharField(max_length=200, default="")
	subject = models.CharField(max_length=200, default="")
	user = models.ForeignKey(User,on_delete=models.CASCADE,default="")
	author = models.CharField(max_length=200, default="")
	sources = models.TextField(default="")
	date = models.DateField(default="")
