"""
URL configuration for hardware_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from hardware_store import settings
from repair_and_sale.views import ListRepairAPIView, ListCategoryAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/repair/list/', ListRepairAPIView.as_view(), name='list of repair'),
    path('api/category/list/', ListCategoryAPIView.as_view(), name='list of category'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
