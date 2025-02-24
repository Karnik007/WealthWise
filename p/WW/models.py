from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    emoji = models.CharField(max_length=100, default='💰')
    def __str__(self):
        return f"{self.source} - {self.currency.symbol}{self.amount}"

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    emoji = models.CharField(max_length=100, default='🛒')
    
    def __str__(self):
        return f"{self.category} - {self.currency.symbol}{self.amount}"

