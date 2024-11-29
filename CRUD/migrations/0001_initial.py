# Generated by Django 5.1.3 on 2024-11-15 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('department', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
