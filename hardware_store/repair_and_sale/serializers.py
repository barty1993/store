from rest_framework import serializers

from repair_and_sale.models import RepairCategory


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    image_url = serializers.ImageField()

    class Meta:
        model = RepairCategory
        fields = '__all__'


class RepairSerializer(serializers.Serializer):
    title = serializers.CharField()
    price = serializers.DecimalField(max_digits=8, decimal_places=2)


class FullCategorySerializer(CategorySerializer):
    repairs = RepairSerializer(many=True)


class FullRepairSerializer(RepairSerializer):
    category = CategorySerializer()
