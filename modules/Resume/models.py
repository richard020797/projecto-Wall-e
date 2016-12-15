from django.db import models
from modules.Sessions import model

class Resume(models.Model):
	id_resume = models.AutoField(primary_key=True)
	id_session = models.ForeignKey(Session, on_delete=models.Cascade,default="")
	original_text = models.TextField(default = "")
	resume_text = models.TextField(default = "")
	key_words = models.TextField(default = "")
