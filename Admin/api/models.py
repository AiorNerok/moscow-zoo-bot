from django.db import models

class Animals(models.Model):
     name: str = models.CharField(max_length=255)
     src:str = models.CharField(max_length=150)
     link_to_more_info: str = models.CharField(max_length=255)
     
     # guardian = models.ForeignKey()

     def __str__(self):
          return self.name
     

class Users(models.Model):
     user_id: str = models.CharField(max_length=255)
     select_lang: str = models.CharField(max_length=10)

