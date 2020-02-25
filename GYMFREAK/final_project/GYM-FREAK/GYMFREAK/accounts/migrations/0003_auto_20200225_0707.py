# Generated by Django 3.0.2 on 2020-02-25 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_gym'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='gym',
            name='services',
        ),
        migrations.AddField(
            model_name='gym',
            name='services',
            field=models.ManyToManyField(to='accounts.Services'),
        ),
    ]
