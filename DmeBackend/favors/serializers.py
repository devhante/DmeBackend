from rest_framework import serializers
from DmeBackend.favors.models import Account, Menu, Favor
# , LANGUAGE_CHOICES, STYLE_CHOICES


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('account_id', 'account_email', 'account_pw')


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('menu_id', 'menu_name')


class FavorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favor
        fields = ('account_id', 'menu_id')

