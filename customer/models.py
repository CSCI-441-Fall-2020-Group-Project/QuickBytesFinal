from django.db import models


# Create your models here.


class Customer(models.Model):
    user_name = models.CharField(max_length=20, null=True, blank=True)
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=20, null=True, blank=True)
    street_address = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=20, null=True, blank=True)


    def __str__(self):
        return self.user_name + " - " + str(self.id)



class Complaint(models.Model):
    BOOL_CHOICES = ((True, 'Yes'),(False,'No'))

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, to_field='id', db_column='customer', null=True, blank=True)
    message = models.CharField(max_length=250, null=True, blank=True)
    in_restaurant = models.BooleanField(choices=BOOL_CHOICES)
    time_placed = models.DateTimeField(auto_now=True, null=True, blank=True)


class Discount(models.Model):
    discount_percentage = models.IntegerField(null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, to_field='id', db_column='customer', null=True, blank=True)
    date = models.DateTimeField(auto_now=True, null=True, blank=True)
    reason = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return str(self.customer.first_name) + ' - ' + self.reason + ' - ' + str(self.discount_percentage) + '%'