from django.db import models

# Create your models here.
class Busser_Supplies_Requests(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    spray_bottle = models.BooleanField(default=False)
    sanitizing_cloth = models.BooleanField(default=False)
    carrying_tray = models.BooleanField(default=False)
    request_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Table_Status(models.Model):
    statusChoices = [
        ('Available', 'Available'),
        ('Occupied', 'Occupied'),
        ('Dirty', 'Dirty'),
        ('Closed', 'Closed'),
        ('Reserved', 'Reserved'),
    ]

    tableSections = [
        ('A1', 'A1'),
        ('B1', 'B1'),
        ('C1', 'C1'),
        ('A2', 'A2'),
        ('B2', 'B2'),
        ('C2', 'C2'),
        ('A3', 'A3'),
        ('B3', 'B3'),
        ('C3', 'C3'),
    ]

    seats = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
    ]

    table = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
    ]

    server = models.CharField(max_length=255, null=True, blank=True)
    section = models.CharField(max_length=255, choices=tableSections)
    table = models.IntegerField(choices=table)
    seats = models.IntegerField(choices=seats)
    status = models.CharField(max_length=255, choices=statusChoices)

    def __str__(self):
        return 'Table: %d | Section: %s' % (self.table, self.section)