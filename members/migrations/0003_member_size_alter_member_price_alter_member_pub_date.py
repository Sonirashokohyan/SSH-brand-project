# Generated by Django 4.2.4 on 2023-08-23 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_price_member_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='size',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='price',
            field=models.IntegerField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='pub_date',
            field=models.DateField(default='', null=True),
        ),
    ]