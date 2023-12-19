from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.translation import gettext as _
from ckeditor.fields import RichTextField
from django_resized import ResizedImageField
import datetime

STATUS = ((0, "Draft"), (1, "Published"))


class Wine(models.Model):
    YEAR_CHOICES = []
    for r in range(1940, (datetime.datetime.now().year + 1)):
        YEAR_CHOICES.append((r, r))
    TYPE_OF_WINE = (
        ("cabernet sauvignon", "Cabernet Sauvignon"),
        ("pinot grigio", "Pinot Grigio"),
        ("malbec", "Malbec"),
        ("sauvignon blanc", "Sauvignon blanc"),
        ("merlot", "Merlot"),
        ("pinot noir", "Pinot noir"),
        ("chardonnay", "Chardonnay"),
    )

    COLOUR = (
        ("red", "Red"),
        ("white", "White"),
        ("rose", "Rose"),
        ("sparkling", "Sparkling"),
        ("fortified", "Fortified"),
    )

    COUNTRY = (
        ("france", "France"),
        ("spain", "Spain"),
        ("italy", "Italy"),
        ("australia", "Australia"),
        ("south africa", "South Africa"),
        ("argentina", "Argentina"),
        ("america", "America"),
        ("portugal", "Portugal"),
    )

    """
    A model to create and manage wines
    """
    user = models.ForeignKey(
        User, related_name="wine_owner", on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null=False, blank=False)
    year = models.IntegerField(
        _("year"), choices=YEAR_CHOICES, default=datetime.datetime.now().year
    )
    type_of_wine = models.CharField(
        max_length=50, choices=TYPE_OF_WINE, default="Cabernet Sauvignon"
    )
    colour = models.CharField(max_length=50, choices=COLOUR, default="Red")
    country = models.CharField(
        max_length=50, choices=COUNTRY, default="France")
    description = models.CharField(max_length=2000, null=False, blank=False)
    image = ResizedImageField(
        size=[400, 400], quality=75, upload_to='wines/', force_format='WEBP',
        blank=False, null=False)
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    posted_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-posted_on"]

    def __str__(self):
        return self.title
