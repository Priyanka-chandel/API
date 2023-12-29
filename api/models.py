from django.db import models

# Create your models here.

#creating company model
class company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=(('IT','IT'),('Non IT','Non IT'),('Mobile phones','Mobile phones'),('Business company','Business company')))

    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    about=models.TextField()
    position=models.CharField(max_length=100,choices=(('Manager','Manager'),('Software Developer','Software Developer'),('Project Leader','Project Leader')))

    company=models.ForeignKey(company, on_delete=models.CASCADE)

