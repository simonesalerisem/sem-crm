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
    
class Order(models.Model):
    name = models.CharField(max_length=200)
    customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.CASCADE)

    def total_hours(self):
        return self.jobs.aggregate(total=models.Sum('hours'))['total'] or 0

    def __str__(self):
        return self.name

class Job(models.Model):
    order = models.ForeignKey(Order, related_name='jobs', on_delete=models.CASCADE)
    date = models.DateField()
    hours = models.DecimalField(max_digits=3, decimal_places=1, choices=[(x/2, x/2) for x in range(1, 17)])
    description = models.CharField(max_length=300)
    
    def __str__(self):
        return f'{self.description} on {self.date}'