from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class Bill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    BillName = models.CharField(max_length=255)
    Duedate = models.DateField()
    Billamount = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.billamount
