from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    uemail = models.CharField(max_length=30)
    ushou = models.CharField(max_length=30,null=True)
    uaddress = models.CharField(max_length=100,null=True)
    uyoubian=models.CharField(max_length=6,null=True)
    uphone = models.CharField(max_length=11,null=True)


