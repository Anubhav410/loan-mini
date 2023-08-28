# Generated by Django 4.2.4 on 2023-08-28 04:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='approved_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='loan',
            name='denied_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='loan',
            name='paid_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='loan',
            name='requested_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='repayments',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='repayments',
            name='failed_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='repayments',
            name='paid_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='repayments',
            name='repayment_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]