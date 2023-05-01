from django.db import models


class RepairCategory(models.Model):
    name = models.CharField(max_length=50)
    image_url = models.ImageField(upload_to="repair_category/")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'repair_category'


class Repair(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category_id = models.ForeignKey(RepairCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = 'repair'