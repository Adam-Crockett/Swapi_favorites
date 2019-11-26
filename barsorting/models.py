from django.db import models
import random

# Create your models here.


class TimesSorted(models.Model):
    """
    Save to the Database how many times the site has sorted bars.
    """


class BubbleSort(models.Model):
    """
    The Bubble Sort algirthm. For this purpose of visual use we will use yield
    at several points in order to display the information on the Template.
    """


class BarValues(models.Model):
    """
    Create a set of 20 values in a randomized list. These values will corrispond
    to the bars in our visual sorting.
    """

    def __init__(self):
        self.bar_values = self.generate_values()

    def __str__(self):
        return self.bar_values

    def get_bar_values(self):
        return self.bar_values

    def set_bar_values(self):
        self.bar_values = self.generate_values()

    def generate_values(self):
        value_list = []
        count = 0
        while count < 20:
            value_list.append(random.randint(5, 50))
            count += 1
        return value_list
