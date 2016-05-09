from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    ndc_old_id = models.CharField(max_length=10)
    create_date = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=100,blank=True,null=True)
    email = models.EmailField(max_length=255, blank=True,null=True,unique=True, )

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.get_full_name()