# Generated by Django 4.2.4 on 2023-08-28 04:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('currency', models.CharField(default='INR', max_length=5)),
                ('term', models.IntegerField()),
                ('frequency', models.IntegerField(default='weekly')),
                ('status', models.CharField(default='pending')),
                ('requested_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='my_loans', to=settings.AUTH_USER_MODEL)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='assigned_loans', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Repayments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('currency', models.CharField(default='INR', max_length=5)),
                ('status', models.CharField(default='pending')),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.loan')),
                ('payer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
