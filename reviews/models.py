from django.db import models
from django.db.models import ImageField
import numpy as np
import  PIL
from PIL import Image


class Product(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(default='Please add a description')
    image = models.ImageField(upload_to = "static/images/products", default='static/images/products/image.jpg' )
    
    def average_rating(self):
        all_ratings = list(map(lambda x: x.rating, self.review_set.all()))
        return np.mean(all_ratings)
        
    def __unicode__(self):
        return self.name

class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    product = models.ForeignKey('Product', on_delete=models.PROTECT)
    pub_date = models.DateTimeField('date published')
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)
