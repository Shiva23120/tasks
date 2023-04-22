from django.db import models
import uuid 
from django.contrib.auth.models import User
from datetime import date
# Create your models here.
class  Task (models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,related_name='tasks')
    SUCCESS_TYPE=(('successfull','successfull'),
    ('unsuccessfull','unsuccessfull'),)
    title=models.CharField(max_length=200)
    description= models.TextField(null=True,blank=True)
    due_date=models.CharField(max_length=140)
    status=models.CharField(max_length=200,choices=SUCCESS_TYPE)
    id = models.UUIDField(default=uuid.uuid4 , unique=True ,primary_key=True,editable=False)
    
    def __str__(self):
        return self.title

class  Comment (models.Model):
    
    comment_owner=models.OneToOneField(Task, on_delete=models.CASCADE)
    comment= models.TextField(null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4 , unique=True ,primary_key=True,editable=False)
    
    def __str__(self):
        return self.comment


    
