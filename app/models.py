from django.db import models

# Create your models here.
class EmployeeModel(models.Model):
    eid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    salary=models.DecimalField(max_digits=10,decimal_places=3)
    conatct=models.IntegerField()
    email=models.EmailField()
    pasword=models.IntegerField()
