from django.db import models
from django.contrib.postgres.fields import ArrayField

   
class Contractor(models.Model):
    company_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    p_iva = models.CharField(max_length=20, verbose_name="P.IVA")
    cf = models.CharField(max_length=20, verbose_name="CF")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name
    

class Customer(models.Model):
    company_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    p_iva = models.CharField(max_length=20, verbose_name="P.IVA")
    cf = models.CharField(max_length=20, verbose_name="CF")
    created_at = models.DateTimeField(auto_now_add=True)
    contractor = models.ForeignKey(Contractor, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.company_name
    

class Contact(models.Model):
    customer = models.ForeignKey(Customer, related_name='contacts', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    position = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'