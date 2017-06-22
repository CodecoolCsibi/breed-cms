from django.db import models
from PIL import Image
from image_cropping import ImageRatioField


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

    name = models.CharField(max_length=50, unique=True)
    date_of_birth = models.DateField('date of birth')
    gender = models.CharField(max_length=1, choices=GENDER, default=MALE)
    status = models.CharField(max_length=1, choices=STATUS, default=AVAILABLE)
    color = models.CharField(max_length=2, choices=COLOR, default=TABBY)
    picture = models.ImageField(blank=True, upload_to='media/images/')
    cropping = ImageRatioField('picture', '50x50')
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return 'name: ' + self.name + ', gender: ' + self.gender + ', status: ' + self.status + ', color: ' + self.color + ', description: ' + self.description
