from django.db import models

# Model Structure
# The model should hold the favorites in the db


class Favorites(models.Model):
    name = models.CharField(max_length=30)
    item_type = models.CharField(max_length=10)
    swapi_url = models.CharField(max_length=50)
    favorite_count = models.IntegerField()
