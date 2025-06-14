from django.db import models

class Student(models.Model):
    fname=models.CharField(max_length=100)
    lname = models .CharField(max_length=100)
    address = models.TextField()
    cname=models.CharField(max_length=100)
    rank=models.IntegerField()
    date_of_joined=models.DateField()

    def __str__(self):
        return self.fname
