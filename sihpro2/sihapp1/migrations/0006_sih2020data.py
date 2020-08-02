# Generated by Django 3.0.8 on 2020-08-02 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sihapp1', '0005_auto_20200801_2304'),
    ]

    operations = [
        migrations.CreateModel(
            name='sih2020data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_Location', models.CharField(max_length=100)),
                ('a_Age', models.IntegerField()),
                ('a_Gender', models.CharField(max_length=100)),
                ('a_Bacteria', models.IntegerField()),
                ('a_Level', models.IntegerField()),
                ('a_Year', models.IntegerField()),
                ('c_Cases', models.BigIntegerField()),
            ],
        ),
    ]