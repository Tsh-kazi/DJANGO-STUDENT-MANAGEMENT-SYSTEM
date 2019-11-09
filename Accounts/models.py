from django.db import models

# Create your models here.


class ClientTable(models.Model):
    client_id = models.CharField(primary_key=True),
    f_name = models.CharField(max_length=20),
    l_name = models.CharField(max_length=20),
    b_date = models.CharField(max_length=20),
    email = models.CharField(max_length=20),
    tell_no = models.CharField(max_length=20),
    gender = models.CharField(max_length=20),
    country = models.CharField(max_length=20),
    city = models.CharField(max_length=20),
    class Meta:
        db_table = ["Customers"]
        

class StaffTable(models.Model):
    staff_id = models.CharField(primary_key=True),
    f_name = models.CharField(max_length=20),
    l_name = models.CharField(max_length=20),
    b_date = models.CharField(max_length=20),
    email = models.CharField(max_length=20),
    tell_no = models.CharField(max_length=20),
    gender = models.CharField(max_length=20),
    country = models.CharField(max_length=20),
    city = models.CharField(max_length=20),
    religion = models.CharField(max_length=20),
    class Meta:
        db_table = ["Staffs"]
        
