# Generated by Django 4.1.7 on 2023-03-22 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=50)),
                ('about', models.TextField()),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('IT', 'IT'), ('NON IT', 'NON IT'), ('Mobile Phones', 'Mobile Phones')], max_length=100)),
                ('added_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
