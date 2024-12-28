from django.db import models


class Categories(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Goods(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    decs = models.CharField(max_length=255)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return self.categories
