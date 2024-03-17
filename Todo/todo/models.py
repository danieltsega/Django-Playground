from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=200)
    done = models.IntegerField(default=0)

    def __str__(self):
        return self.task