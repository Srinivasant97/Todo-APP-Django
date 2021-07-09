from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TodoList(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	task=models.CharField(max_length= 200)
	details=models.TextField()
	completed=models.BooleanField()
	Date=models.DateTimeField()

	def __str__(self):
		return self.task
