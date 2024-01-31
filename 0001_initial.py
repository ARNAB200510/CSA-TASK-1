# Generated by Django 4.2.9 on 2024-01-31 17:40

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
            name='Eatery_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Food_name', models.CharField(max_length=100)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('Eatery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FDA_By_CSA.eatery_details')),
            ],
        ),
        migrations.CreateModel(
            name='Rating_eatery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rating_Points', models.PositiveIntegerField()),
                ('BITS_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Eatery_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FDA_By_CSA.eatery_details')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rating_Points', models.PositiveIntegerField()),
                ('BITS_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Item_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FDA_By_CSA.items')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('BITS_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Items', models.ManyToManyField(to='FDA_By_CSA.items')),
            ],
        ),
    ]
