from django.db import models




class Item(models.Model):

    item = models.CharField(max_length=250)

    def __str__(self):
        return self.item
        
    
    class Meta:
        verbose_name_plural = "Items"


class Category(models.Model):

    title = models.CharField(max_length=250)
    items =  models.ManyToManyField(Item, through="Fellowship")


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Categories"





class Fellowship(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


