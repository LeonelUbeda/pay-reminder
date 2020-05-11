from django.shortcuts import render
from rest_framework import viewsets
from .models import Payment, PaymentGroup, PaymentTracking
from .serializers import PaymentsSerializer, PaymentGroupSerializer, PaymentTrackingSerializer
from rest_framework.permissions import IsAuthenticated



class PaymentsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PaymentsSerializer

    def get_queryset(self):
        user = self.request.user
        print(self.request.user)
        return Payment.objects.filter(user=user.id)
    
    

    #def perform_create(self, serializer):
    #    return serializer.save(user=self.request.user)

class PaymentGroupViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PaymentGroupSerializer
    def get_queryset(self):
        user = self.request.user
        return PaymentGroup.objects.filter(user=user)

class PaymentTrackingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PaymentTrackingSerializer
    
    def get_queryset(self):
        user = self.request.user
        payment = self.request.query_params.get('username', None)
        return PaymentTracking.objects.filter(payment__user=user)