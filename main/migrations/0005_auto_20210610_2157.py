# Generated by Django 3.2.4 on 2021-06-10 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_consultant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(default='', max_length=20, verbose_name='Бренд')),
                ('model', models.CharField(default='', max_length=20, verbose_name='Модель')),
                ('bodymodel', models.CharField(default='', max_length=20, verbose_name='Модель кузова')),
                ('wheelposition', models.CharField(default='', max_length=10, verbose_name='Позиция руля')),
                ('drivebool', models.CharField(default='', max_length=5, verbose_name='Полный привод')),
                ('type', models.CharField(default='', max_length=8, verbose_name='Тип')),
                ('bodytype', models.CharField(default='', max_length=20, verbose_name='Тип кузова')),
                ('bodynumber', models.IntegerField(verbose_name='Номер кузова')),
                ('enginenumber', models.IntegerField(verbose_name='Номер двигателя')),
                ('enginevolume', models.IntegerField(verbose_name='Объём двигателя')),
                ('enginepower', models.IntegerField(verbose_name='Мощность двигателя')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('year', models.IntegerField(verbose_name='Год выпуска')),
                ('mileage', models.IntegerField(verbose_name='Милиаж')),
            ],
            options={
                'verbose_name': 'Машина',
                'verbose_name_plural': 'Машины',
            },
        ),
        migrations.AlterModelOptions(
            name='consultant',
            options={'verbose_name': 'Консультант', 'verbose_name_plural': 'Консультанты'},
        ),
    ]