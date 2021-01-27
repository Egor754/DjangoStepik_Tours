from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('tours', '0003_auto_20210119_0224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tours',
            name='picture',
            field=models.URLField(max_length=600, verbose_name='Ссылка на картинку'),
        ),
    ]
