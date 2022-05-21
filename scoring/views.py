from django.db.transaction import atomic
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Receipt
from .task import async_create
from scoring.serializers import ReceiptSerializer


class ReceiptApiView(ModelViewSet):
    serializer_class = ReceiptSerializer
    permission_classes = [AllowAny]
    queryset = Receipt.objects.all()

    @atomic
    def create(self, request, *args, **kwargs):
        submit_score_serializer = ReceiptSerializer(data=request.data)
        if submit_score_serializer.is_valid():
            async_create.delay(submit_score_serializer.data)
        else:
            return Response('error')

    @atomic
    def get(self, request, *args, **kwargs):
        submit_score_serializer = ReceiptSerializer(data=request.data)
        if submit_score_serializer.is_valid():
            async_create.delay(submit_score_serializer.data)
            return Response('ok')
        else:
            return Response('error')
