from email.policy import default
from django.db import models
from time import strftime
import re

class UserManager (models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData["first_name"]) < 2:
            errors["first_name"] = "First Name should be at least 2 characters"
        if len(postData["last_name"]) < 2:
            errors["last_name"] = "Last Name should be at least 2 characters"
        if len(postData["password"]) < 8:
            errors["password"] = "Password should be at least 8 characters"

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        if postData["password"]!=postData["pass_confirm"]:
            errors["cpassword"]="Passwords does not match"
        for E in User.objects.all():
            if postData['email']==E.email:
                errors["DuplicateEmail"]="This Email is Taken"
        
        # List=postData['date']
        # Year=List[0]+List[1]+List[2]+List[3]
        # Month=List[5]+List[6]
        # Day=List[8]+List[9]
        # if  int(Year)>int(strftime ("%Y")):
        #     errors["date"] = "invalid date"
        # if int(Year)==int(strftime ("%Y")):
        #     if int(Month)>int(strftime ("%m")):
        #         errors["date"] = "invalid date"
        # if int(Month)==int(strftime ("%m")) :  
        #     if int(Day)>int(strftime ("%d")):
        #         errors["date"] = "invalid date"
        return errors



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects=UserManager()

class PlanManager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        # if len(postData["Species"]) < 6:
        #     errors["Species"] = "First Name should be at least 6 characters" 
        return errors


class Plan (models.Model):
    Species = models.CharField(max_length=255)
    location=models.CharField(max_length=15,null=True)
    relaseDate= models.DateTimeField()
    description = models.TextField()
    user=models.ForeignKey(User, related_name="plans_uploded", on_delete = models.CASCADE, null=True )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=PlanManager()

