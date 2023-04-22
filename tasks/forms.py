from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from tasks.models import Task,Comment

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','email','username','password1','password2']
        labels={
            'first_name':'Name',
        }


    def __init__(self,*args,**kwargs):
        super(CustomUserCreationForm, self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class TaskForm(ModelForm):
    class Meta:
        model=Task
        fields=['title','description','due_date','status']
    def __init__(self,*args,**kwargs):
        super(TaskForm, self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class CommentForm(ModelForm):
    class Meta:
        model=Comment
        fields=['comment']
    def __init__(self,*args,**kwargs):
        super(CommentForm, self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class CategoryForm(ModelForm):
    class Meta:
        model=Task
        fields=['status']
    
    def __init__(self,*args,**kwargs):
        super(CategoryForm, self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})