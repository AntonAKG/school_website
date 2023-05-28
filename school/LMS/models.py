from django.db import models


class LMS(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20 )