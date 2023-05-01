from django.contrib import admin
from .models import RepairCategory, Repair

admin.site.register([Repair, RepairCategory])
