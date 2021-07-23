from django.db import models

# Create your models here.
class User(models.Model):


    firstname = models.CharField(max_length=100, null=False, blank=False)
    lastname = models.CharField(max_length=100, null=False, blank=False)
    email = models.CharField(max_length=100, null=False, blank=False)
    password = models.CharField(max_length=100, null=False, blank=False)
    user_id = models.IntegerField()

    def __str__(self):
        return self.firstname