from django.db import models

class Session(models.Model):
	id_session = models.AutoField(primary_key=True)
	title = models.CharField(max_length=200, default="")
	subject = models.CharField(max_length=200, default="")
	#user = models.ForeignKey(default="")
	author = models.CharField(max_length=200, default="")
	sources = models.TextField(default="")
	date = models.DateField(default="")
