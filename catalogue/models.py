from django.db import models

# Create your models here.
class Catalogue(models.Model):
    baseid = models.CharField(max_length=6)
    name = models.CharField(max_length=255)
    notes = models.TextField

class User(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=255)
    admin = models.BooleanField(default=False)

class PaintScheme(models.Model):
    name = models.CharField(max_length=255)
    notes = models.TextField
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Collection(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    mini = models.ForeignKey(Catalogue, on_delete=models.CASCADE)
    paint = models.ForeignKey(PaintScheme, blank=True, null=True, on_delete=models.CASCADE)
    notes = models.TextField
