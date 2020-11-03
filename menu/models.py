from django.db import models


# Create your models here.
class Menu_Item(models.Model):
    class MenuTypes(models.TextChoices):
        APPETIZER = "Appetizer"
        ENTREE = "Entree"
        DESSERT = "Dessert"
        WINE = "Wine"
        BEER = "Beer"
        COCKTAIL = "Cocktail"
        SIDE = "Side"

    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 250)
    price = models.DecimalField(max_digits = 4, decimal_places= 2)
    item_type = models.CharField(max_length = 10, choices=MenuTypes.choices, default=MenuTypes.APPETIZER)
      
    
    def __str__(self):
        return self.name + ' - $' + str(self.price)
