from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('departure', models.CharField(max_length=50, verbose_name='Отправление')),
                ('picture', models.URLField(max_length=300, verbose_name='Ссылка на картинку')),
                ('price', models.IntegerField(null=True, verbose_name='Стоимость')),
                ('stars', models.IntegerField(null=True, verbose_name='Звёзды')),
                ('country', models.CharField(max_length=100, verbose_name='Страна')),
                ('nights', models.IntegerField(null=True, verbose_name='Длительность')),
                ('date', models.CharField(max_length=50, verbose_name='Дата')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликован')),
            ],
            options={
                'verbose_name': 'Тур',
                'verbose_name_plural': 'Туры',
            },
        ),
    ]
