from django.db import models


class RepairCategory(models.Model):
    name = models.CharField(max_length=50)
    image_url = models.ImageField(upload_to="repair_category/")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'repair_category'
        default_related_name = 'categories'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории услуг'


class Repair(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(RepairCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = 'repair'
        default_related_name = 'repairs'
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class UsedItem(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True, null=False)
    image_url = models.ImageField(upload_to="used_item/")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'used_item'
        verbose_name = 'б/у товар'
        verbose_name_plural = 'б/у товары'
