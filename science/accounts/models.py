
from django.db import models

class RegisterUser(models.Model):
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact = models.CharField(max_length=30)  
    email = models.EmailField(unique=True)
    




    