# Generated by Django 3.2.12 on 2022-04-06 11:27

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bonds',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('bond_name', models.CharField(max_length=40, validators=[django.core.validators.MinLengthValidator(3)])),
                ('number_of_bonds', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10, 0), django.core.validators.MinValueValidator(1)])),
                ('selling_price_mxn', models.FloatField(validators=[django.core.validators.MaxValueValidator(100000000.0), django.core.validators.MinValueValidator(0.0)])),
                ('status', models.CharField(choices=[('PU', 'Published'), ('SO', 'Sold')], default='PU', max_length=2)),
                ('buyer_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='buyer_id', to=settings.AUTH_USER_MODEL)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]