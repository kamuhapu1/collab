from django.db import models

class TableBooking(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    day = models.CharField(max_length=20)
    hour = models.CharField(max_length=10)
    persons = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} - {self.day} {self.hour} ({self.persons})"

