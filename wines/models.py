from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.translation import gettext as _
from ckeditor.fields import RichTextField
import datetime

STATUS = ((0, "Draft"), (1, "Published"))


class Wine(models.Model):

    YEAR_CHOICES = []
    for r in range(1940, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r, r))

    WINE_TYPE = (
        ('cabernet sauvignon', 'Cabernet Sauvignon'),
        ('pinot grigio', 'Pinot Grigio'),
        ('malbec', 'malbec'),
        ('sauvignon blanc', 'Sauvignon blanc'),
        ('merlot', 'Merlot'),
        ('pinot noir', 'Pinot noir'),
        ('chardonnay', 'Chardonnay'),
    )

    WINE_COLOUR = (
        ('red', 'Red'),
        ('white', 'White'),
        ('rose', 'Rose'),
        ('sparkling', 'Sparkling'),
        ('fortified', 'Fortified'),
    )

    COUNTRY = (
        ('france', 'France'),
        ('spain', 'Spain'),
        ('italy', 'Italy'),
        ('australia', 'Australia'),
        ('south africa', 'South Africa'),
        ('argentina', 'Argentina'),
        ('america', 'America'),
        ('portugal', 'Portugal'),
    )

    """
    A model to create and manage wines
    """
    user = models.ForeignKey(
        User, related_name='wine_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null=False, blank=False)
    slug = models.SlugField(max_length=200, unique=True)
    year = models.IntegerField(
        _('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    type_of_wine = models.CharField(
        max_length=50, choices=WINE_TYPE, default='Cabernet Sauvignon')
    colour = models.CharField(
        max_length=50, choices=WINE_COLOUR, default='Red')
    country = models.CharField(
        max_length=50, choices=COUNTRY, default='France')
    description = RichTextField(max_length=10000, null=False, blank=False)
    image = CloudinaryField('image', default='placeholder')
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    posted_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-posted_on']

    def __str__(self):
        return self.title
