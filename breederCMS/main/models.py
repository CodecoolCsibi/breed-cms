from django.db import models


class AnimalEntry(models.Model):

    AVAILABLE = 'A'
    RESERVED = 'R'
    SOLD = 'S'
    STATUS = (
        (AVAILABLE, 'Available'),
        (RESERVED, 'Reserved'),
        (SOLD, 'Sold'),
    )

    MALE = 'M'
    FEMALE = 'F'
    GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )

    TABBY = 'TA'
    COLORPOINT = 'CP'
    COLOR = ((TABBY, 'Tabby'), (COLORPOINT, 'Colorpoint'))

    name = models.CharField(max_length=50)
    date_of_birth = models.DateField('date of birth')
    gender = models.CharField(max_length=1, choices=GENDER, default=MALE)
    status = models.CharField(max_length=1, choices=STATUS, default=AVAILABLE)
    color = models.CharField(max_length=2, choices=COLOR, default=TABBY)
    picture = models.ImageField(blank=True)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name + self.gender + self.status + self.color + self.description
