from django.db import models

class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    account_email = models.CharField(max_length=40, unique=True, null=False)
    account_pw = models.CharField(max_length=20, null=False)

class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    menu_name = models.CharField(max_length=30, unique=True, null=False)

class Favor(models.Model):
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('account_id', 'menu_id')