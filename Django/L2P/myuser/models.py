from django.db import models

# Create your models here.
class User_details(models.Model):
    first_name = models.CharField(max_length = 264, primary_key = True)
    last_name = models.CharField(max_length = 264)
    email = models.CharField(max_length = 264)

    def __str__(self):
        return self.first_name
