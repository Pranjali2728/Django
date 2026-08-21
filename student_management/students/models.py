from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField(unique=True)
    email = models.EmailField()
    course = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name