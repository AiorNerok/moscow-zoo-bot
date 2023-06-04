from django.db import models

class Animals(models.Model):
     name: str = models.CharField(max_length=255)
     src:str = models.CharField(max_length=150)
     link_to_more_info: str = models.CharField(max_length=255)

     def __str__(self):
          return self.name