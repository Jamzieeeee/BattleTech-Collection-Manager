# Taken from https://www.abidibo.net/blog/2014/05/22/check-if-user-belongs-group-django-templates/
from django import template
from django.contrib.auth.models import Group 

register = template.Library() 

# Creates a django template filter to check if a user is in the given group
@register.filter(name='has_group') 
def has_group(user, group_name):
    group = Group.objects.filter(name=group_name)
    if group:
        group = group.first()
        return group in user.groups.all()
    else:
        return False