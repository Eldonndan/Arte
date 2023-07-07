# Generated by Django 4.2.2 on 2023-07-06 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obra',
            name='id_obra',
            field=models.AutoField(db_column='id_obra', primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='ObraFav',
            fields=[
                ('id_fav', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=50)),
                ('id_obra', models.ForeignKey(db_column='id_obra', on_delete=django.db.models.deletion.CASCADE, to='app.obra')),
            ],
        ),
    ]
