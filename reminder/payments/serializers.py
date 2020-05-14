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
        fields = ('payment_day', 'name', 'group', 'created_at', 'frequency', 'state', 'user', 'id')
        
    def __init__(self, *args, request_user=None, **kwargs):
        super(PaymentsSerializer, self).__init__(*args, **kwargs)
        #Con esto me aseguro de que el dropdown de la interfaz solo salgan los grupos del usuario.
        #Ademas, por lo que vi, no deja ingresar manualmente un grupo que no sea tuyo. 2x1 XD
        if 'request' in self.context:
            print('chaale')
            self.fields['group'].queryset = PaymentGroup.objects.filter(user=self.context['request'].user.id)
        




        


class PaymentTrackingSerializer(serializers.ModelSerializer):
    paid_date = serializers.DateField()
    id = serializers.ReadOnlyField()
    class Meta:
        model = PaymentTracking
        fields = ('payment', 'paid_date', 'id')