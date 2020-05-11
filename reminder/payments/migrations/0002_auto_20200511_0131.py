# Generated by Django 3.0.6 on 2020-05-11 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('payments', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentgroup',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
        migrations.AddField(
            model_name='payment',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payments.PaymentGroup'),
        ),
    ]
