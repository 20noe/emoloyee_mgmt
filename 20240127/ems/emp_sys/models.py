from django.db import models

# Create your models here.

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    def __str__(self):
        return self.name + ' '+ str(self.id)
    

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    post = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete = models.CASCADE)

    def __str__(self):
        return self.firstname + ' ' + self.lastname


