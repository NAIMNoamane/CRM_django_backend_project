# Generated by Django 5.1.1 on 2024-09-22 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('adress', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('Region', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=20)),
            ],
        ),
    ]
