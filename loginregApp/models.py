from django.db import models
import re

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        emailMatch = User.objects.filter(email=postData['email'])
        if len(postData['fname']) < 2:
            errors["fnamereq"] = "First Name needs to be at least 2 characters"
        if len(postData['lname']) < 2:
            errors["lnamereq"] = "Last Name needs to be at least 2 characters"
            
        if len(postData['email']) < 5:
            errors["emailreq"] = "Email is required"
        elif not EMAIL_REGEX.match(postData['email']):           
            errors['emailpattern'] = "Invalid email address!"
        if len(emailMatch)>0:
            errors['duplicateEmail'] = "Email is already taken"
            
            
        if len(postData['pw']) <3:
            errors["pwreq"] = "Passwords needs to be at least 3 characters"
            
        if postData['pw'] !=postData['cpw']:
            errors['cpwmatch'] = "Confirm password must match"
            
        return errors
    
    def loginValidator(self, postData ):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        emailMatch = User.objects.filter(email=postData['email'])
        print(emailMatch)
        if len(postData['email']) < 5:
            errors["emailreq"] = "Email is required"
        elif not EMAIL_REGEX.match(postData['email']):           
            errors['emailpattern'] = "Invalid email address!"
        elif len(emailMatch) == 0:
            errors['noemail']= "Email is not registered"
        else:
            if emailMatch[0].password != postData['pw']:
                errors['pwmatch'] = "Incorrect Password!"
                
        return errors
            
        
            
        
            
            
            
        


# Create your models here.
class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()
    