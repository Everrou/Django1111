# Generated by Django 4.2.5 on 2023-10-09 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kino',
            name='image',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='born',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='country',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='fname',
            field=models.CharField(max_length=20, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='lname',
            field=models.CharField(max_length=20, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='agerate',
            name='rate',
            field=models.CharField(choices=[('G', 'G'), ('PG', 'PG'), ('PG-13', 'PG-13'), ('R', 'R'), ('NC-17', 'NC-17')], max_length=20, verbose_name='Рейтинг'),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='director',
            name='fname',
            field=models.CharField(max_length=20, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='director',
            name='lname',
            field=models.CharField(max_length=20, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='kino',
            name='actor',
            field=models.ManyToManyField(to='catalog.actor', verbose_name='Актеры'),
        ),
        migrations.AlterField(
            model_name='kino',
            name='rating',
            field=models.FloatField(verbose_name='Оценка'),
        ),
        migrations.AlterField(
            model_name='kino',
            name='summary',
            field=models.TextField(max_length=500, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='kino',
            name='title',
            field=models.CharField(max_length=20, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='kino',
            name='year',
            field=models.IntegerField(verbose_name='год'),
        ),
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(choices=[('Бесплатно', 'Бесплатно'), ('Базовая', 'Базовая'), ('Супер', 'Супер')], max_length=20, verbose_name='Подписка'),
        ),
    ]
