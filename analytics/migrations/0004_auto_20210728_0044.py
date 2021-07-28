# Generated by Django 3.0.8 on 2021-07-28 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0003_auto_20210728_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='first_score',
            field=models.FloatField(null=True, verbose_name='Score of the highest recommendation'),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='second_score',
            field=models.FloatField(null=True, verbose_name='Score of the second recommendation'),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='third_score',
            field=models.FloatField(null=True, verbose_name='Score of the third recommendation'),
        ),
    ]
