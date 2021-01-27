from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Depart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Отправление')),
                ('ru_departure', models.CharField(max_length=50, null=True, verbose_name='Отправление_RU')),
            ],
            options={
                'verbose_name': 'Отправление',
                'verbose_name_plural': 'Отправления',
            },
        ),
        migrations.RemoveField(
            model_name='tours',
            name='departure',
        ),
        migrations.RemoveField(
            model_name='tours',
            name='is_published',
        ),
        migrations.AddField(
            model_name='tours',
            name='departurt',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='tours.depart'),
        ),
    ]
