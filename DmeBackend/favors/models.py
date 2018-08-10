from django.db import models
# from pygments.lexers import get_all_lexers
# from pygments.styles import get_all_styles

# LEXERS = [item for item in get_all_lexers() if item[1]]
# LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
# STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


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