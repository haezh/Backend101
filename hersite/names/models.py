from django.db import models

# Create your models here.

# django's way of interacting with databases

## Each model has a number of class variables, each of which represents a database field in the model.


class Name(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + " " + self.last_name
