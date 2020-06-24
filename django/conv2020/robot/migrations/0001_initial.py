# Generated by Django 3.0.3 on 2020-04-20 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Msg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('message', models.CharField(blank=True, max_length=1000, null=True)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('star', models.IntegerField(default=0)),
                ('emotion', models.IntegerField()),
            ],
            options={
                'db_table': 'msg',
            },
        ),
    ]