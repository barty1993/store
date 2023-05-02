from django.contrib import admin
from .models import RepairCategory, Repair, UsedItem

admin.site.register([Repair, RepairCategory, UsedItem])
