from django.db import models

class User(models.Model):
    username = models.CharField(primary_key=True, max_length=15)
    age = models.IntegerField()
    phonenumber = models.CharField(max_length=20)

    class Meta:
        db_table = 'User'