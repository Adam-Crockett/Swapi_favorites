from django.db import models

# Model Structure
# The model should hold the favorites in the db


class Favorites(models.Model):
    """
    Favorites selected by users in each catagory and the number of favorites
    for each object.
    """
    objects = models.Manager()
    ITEM_TYPES = (
        ('films', 'Films'),
        ('people', 'People'),
        ('planets', 'Planets'),
        ('species', 'Species'),
        ('starships', 'Starships'),
        ('vehicles', 'Vehicles')
    )
    name = models.CharField(max_length=30, primary_key=True)
    item_type = models.CharField(max_length=1, choices=ITEM_TYPES)
    swapi_url = models.CharField(max_length=50)
    favorite_count = models.IntegerField()

    def __str__(self):
        return self.name
