from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('tours', '0002_auto_20210119_0134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tours',
            name='departurt',
        ),
        migrations.AddField(
            model_name='tours',
            name='departure',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT,
                                    to='tours.depart', verbose_name='Отправление'),
        ),
    ]
