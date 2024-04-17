# Generated by Django 5.0.4 on 2024-04-05 08:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('member_type', models.CharField(choices=[('M', 'Member'), ('AM', 'Associate Member'), ('FM', 'Fellowship Member'), ('NM', 'Non Member')], max_length=2)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('occupation', models.CharField(choices=[('E', 'Employed'), ('UE', 'Unemployed'), ('S', 'Student'), ('R', 'Retired'), ('D', 'Deceased')], max_length=2)),
                ('remarks', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=10)),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='member.member')),
            ],
        ),
    ]
