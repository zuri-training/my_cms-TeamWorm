from django.db import models
from django.contrib.auth.models import User

import sys
sys.path.append("..") # Adds higher directory to python modules path.

from accounts.models import UserProfile


# Create your models here.
class AllTemplates(models.Model):
    name=models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    CATEGORIES = (
        ('agriculture', 'Agriculture'),
        ('tech', 'Tech'),
        ('blog', 'Blog'),
        ('photography', 'Photography'),
        ('sports', 'Sports'),
        ('news', 'News'),
        ('portfolio', 'Portfolio'),
    )
    categories = models.CharField(max_length=15, choices=CATEGORIES)

    def __str__(self) -> str:
        return f"<{self.name}>, <{self.id}>"


class UserTemplate(models.Model):
    template_id=models.OneToOneField(AllTemplates, on_delete=models.CASCADE, verbose_name="id of template")
    user_id=models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"<{self.template_id}>, <{self.user_id}>"



# class FilterTemplates(models.Model):
#     INDUSTRIES = (
#         ('agriculture', 'Agriculture'),
#         ('tech', 'Tech')
#         ('blog', 'Blog')
#         ('photography', 'Photography')
#         ('sports', 'Sports')
#         ('news', 'News')
#         ('portfolio', 'Portfolio')
#     )
#     industries = models.CharField(max_length=1, choices=INDUSTRIES)

#     def __str__(self) -> str:
#         return f"<{self.name}>, <{self.id}>"

