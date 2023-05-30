from rest_framework import serializers

from repair_and_sale.models import RepairCategory, UsedItem


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    image_url = serializers.ImageField()

    class Meta:
        model = RepairCategory
        fields = '__all__'


class RepairSerializer(serializers.Serializer):
    title = serializers.CharField()
    price = serializers.DecimalField(max_digits=8, decimal_places=2)


class UsedItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsedItem
        fields = '__all__'


class BookItemSerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=True, max_length=11)
    message = serializers.CharField(required=True, max_length=100)
    item_name = serializers.CharField(required=True)


class CallRequestSerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=True, max_length=11)
    name = serializers.CharField(required=True, max_length=20)
