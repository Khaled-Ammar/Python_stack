from django.db import models
from time import strftime

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData["title"]) < 3:
            errors["title"] = "Title name should be at least 2 characters"
        if len(postData["network"]) < 4 :
            errors["network"] = "Network field should be at least 3 characters"
        if len(postData["desc"]) >0 and len(postData["desc"]) < 11 :
            errors["desc"] = "Description field should be at least 10 characters"

        List=postData['date']
        Year=List[0]+List[1]+List[2]+List[3]
        Month=List[5]+List[6]
        Day=List[8]+List[9]
        if  int(Year)>int(strftime ("%Y")):
            errors["date"] = "invalid date"
        if int(Year)==int(strftime ("%Y")):
            if int(Month)>int(strftime ("%m")):
                errors["date"] = "invalid date"
        if int(Month)==int(strftime ("%m")) :  
            if int(Day)>int(strftime ("%d")):
                errors["date"] = "invalid date"
            
        return errors


class Show (models.Model):
    title = models.CharField(max_length=255)
    network=models.CharField(max_length=15)
    relaseDate= models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=ShowManager()
