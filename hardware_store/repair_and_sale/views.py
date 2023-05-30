from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from repair_and_sale.models import Repair, RepairCategory, UsedItem
from repair_and_sale.serializers import UsedItemsSerializer, \
    BookItemSerializer, CallRequestSerializer, CategorySerializer, RepairSerializer
from repair_and_sale.services.common_services import all_objects, repairs_filter_by_id
from repair_and_sale.tasks import book_a_product_telegram_task, call_request_telegram_task


class ListRepairAPIView(APIView):

    def get(self, request, **kwargs):
        pk = kwargs.get('pk')
        if not pk:
            return Response(data={"error": "need category id"},
                            status=status.HTTP_400_BAD_REQUEST)
        queryset = repairs_filter_by_id(Repair.objects, pk)
        serializer = RepairSerializer(queryset, many=True)
        return Response(data=serializer.data,
                        status=status.HTTP_200_OK)


class ListCategoryAPIView(APIView):

    def get(self, request):
        queryset = all_objects(RepairCategory.objects)
        serializer = CategorySerializer(queryset, many=True)
        return Response(data=serializer.data,
                        status=status.HTTP_200_OK)


class ListUsedItemsAPIView(ListAPIView):
    queryset = all_objects(UsedItem.objects)
    serializer_class = UsedItemsSerializer


class BookItemAPIView(APIView):

    def post(self, request):
        serializer = BookItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        book_a_product_telegram_task.delay(request.data)
        return Response(status=status.HTTP_200_OK)


class CallRequestAPIView(APIView):

    def post(self, request):
        serializer = CallRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        call_request_telegram_task.delay(request.data)
        return Response(status=status.HTTP_200_OK)
