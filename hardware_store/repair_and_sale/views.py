from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from repair_and_sale.models import Repair, RepairCategory
from repair_and_sale.serializers import FullRepairSerializer, FullCategorySerializer
from repair_and_sale.services.common_services import all_objects, query_debugger


class ListRepairAPIView(APIView):

    def get(self, request):
        queryset = all_objects(Repair.objects, select_related=('category',))
        serializer = FullRepairSerializer(queryset, many=True)
        return Response(data=serializer.data,
                        status=status.HTTP_200_OK
                        )


class ListCategoryAPIView(APIView):

    def get(self, request):
        queryset = all_objects(RepairCategory.objects, prefetch_related=('repairs',))
        serializer = FullCategorySerializer(queryset, many=True)
        return Response(data=serializer.data,
                        status=status.HTTP_200_OK
                        )
