from rest_framework import serializers
from .models import Payment, PaymentGroup, PaymentTracking


class PaymentGroupSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        #Agarra el usuario de la sesion. request.user
        default=serializers.CurrentUserDefault()
    )
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model =  PaymentGroup
        fields = ('user', 'name', 'id')


class PaymentsSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Payment
        fields = ('payment_date', 'name', 'group', 'created_at', 'frequency', 'state', 'user', 'id')
        


class PaymentTrackingSerializer(serializers.ModelSerializer):
    paid_date = serializers.DateField()

    class Meta:
        model = PaymentTracking
        fields = ('payment', 'paid_date')