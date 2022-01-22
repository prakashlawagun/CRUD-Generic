from django.db import models
from django.urls import reverse_lazy


# Create your models here.
class Employee(models.Model):
    ename = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=60)
    salary = models.PositiveIntegerField()

    def __str__(self):
        return self.ename

    def get_delete_employee_url(self):
        return reverse_lazy('ecomapp:CustomerCancelOrderView', args=[self.id])
