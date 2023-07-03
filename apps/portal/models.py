from django.db import models

# Create your models here.


class Product(models.Model):

    title = models.CharField(max_length=250)
    img = models.ImageField(upload_to="products/")


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Products"


