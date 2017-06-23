from django.db import models
from django.forms import ModelForm

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


class AnimalEntry(models.Model):

    name = models.CharField(max_length=50, unique=True)
    date_of_birth = models.DateField('date of birth')
    gender = models.CharField(max_length=1, choices=GENDER, default=MALE)
    status = models.CharField(max_length=1, choices=STATUS, default=AVAILABLE)
    color = models.CharField(max_length=2, choices=COLOR, default=TABBY)
    picture = models.ImageField(blank=True, upload_to='media/images/')
    cropped_picture = models.ImageField(blank=True, upload_to='media/cropped/')
    description = models.CharField(max_length=200, blank=True)
