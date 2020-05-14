from django.db import models
from django.utils import timezone
from user.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)




class PaymentGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments_groups')
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name



class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    created_at = models.DateTimeField()
    payment_day = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(31)])
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

class PaymentByDay(models.Model):
    pass




class PaymentTracking(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='history')
    paid_date = models.DateField()

  
    
    def __str__(self):
        return self.paid_date
