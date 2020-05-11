from django.db import models
from django.utils import timezone
from user.models import User
# Create your models here.


class PaymentGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments_groups')
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name



class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    created_at = models.DateTimeField()
    payment_date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    group = models.ForeignKey(PaymentGroup, on_delete=models.CASCADE, related_name='payments', blank=True, null=True)

    class Frequency(models.IntegerChoices):
        MONTHLY = 1
    
    frequency = models.IntegerField(choices=Frequency.choices)

    class State(models.IntegerChoices):
        ACTIVE = 1
        INACTIVE = 2

    state = models.IntegerField(choices=State.choices)
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        super(Payment, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class PaymentTracking(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='history')
    paid_date = models.DateField()

  
    
    def __str__(self):
        return self.paid_date
