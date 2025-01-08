from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re


# Create your models here.
class Catalogue(models.Model):
    #Catalyst Base IDs are of the form '123', '12-34', 'a1', or '1A-23'
    def validate_baseid(baseid_str):
        pattern=re.compile("^(a\d|\d+(\-\d+)?|1A\-\d+)$")
        if not pattern.match(baseid_str):
            raise ValidationError("Base ID is not legal.") 
    baseid = models.CharField(max_length=6, validators=[validate_baseid])

    name = models.CharField(max_length=255)
    notes = models.TextField(null=True, blank=True)

    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        kilobyte_limit = 500
        if filesize > kilobyte_limit*1024:
            raise ValidationError("Max file size is %sKB" % str(kilobyte_limit))
    image = models.ImageField(upload_to='images/', null=True, blank=True, validators=[validate_image])

class PaintScheme(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    notes = models.TextField(null=True, blank=True)

class Collection(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    mini = models.ForeignKey(Catalogue, on_delete=models.CASCADE)
    paint = models.ForeignKey(PaintScheme, blank=True, null=True, on_delete=models.CASCADE)
    notes = models.TextField(null=True, blank=True)
