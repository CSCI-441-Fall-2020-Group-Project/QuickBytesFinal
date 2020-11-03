from django.db import models
from django.forms import ModelForm

# Create your models here.
class Worker_Complaint(models.Model):
    complaint = models.TextField()

class Customer_Complaint(models.Model):
    status = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    complaint = models.TextField()
    customerName = models.CharField(max_length=255, default=None)
    inRestaurant = models.CharField(max_length=255, choices=status)

class Budget_Table(models.Model):
    status = [
        ('Income', 'Income'),
        ('Expense', 'Expense'),
        ('Other', 'Other'),
    ]
    item_Name = models.CharField(max_length=50) #require
    item_Category = models.CharField(max_length=50, choices=status) #require
    item_Note = models.CharField(max_length=100, default=None)
    item_Date = models.DateField() #require
    item_Amount = models.IntegerField() #require

class Schedule_Table(models.Model): 
    position = [
        ('Chef', 'Chef'),
        ('Server', 'Server'),
        ('Busser', 'Busser'),
        ('Manager', 'Manager'),
        ('Host', 'Host'),
        ('Delivery', 'Delivery'),
    ]
    worker_Name = models.CharField(max_length=50)
    worker_Position = models.CharField(max_length=50, choices=position)
    worker_Start = models.TimeField()
    worker_End = models.TimeField()
    worker_Date = models.DateField()
    worker_Break = models.IntegerField() 


def __str__(self):
    return self.name