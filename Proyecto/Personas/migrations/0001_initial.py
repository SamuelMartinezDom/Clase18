# Generated by Django 4.0.6 on 2022-07-29 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('wager', models.FloatField()),
                ('creation_date', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]