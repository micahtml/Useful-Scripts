from django.db import models
import re

class UserManager(models.Manager):
    def register_validator(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors={}
        if len(postData['fname']) < 2:
            errors['fname']='First name must be at least 2 characters'
        if len(postData['lname']) < 2:
            errors['lname']='First name must be at least 2 characters'
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = ("Invalid email address!")
        elif User.objects.filter(email=postData['email']):
            errors['email'] = 'Email already exists'
        if len(postData['password'])< 8:
            errors['password']= 'Password must be at least 8 characters'
        elif postData['password'] != postData['confirmPW']:
            errors['password'] = 'Password and confirm password must match'
        return errors

class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()