# Generated by Django 5.0.4 on 2024-04-08 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(choices=[('U', 'U'), ('A', 'A')], default='A', max_length=1),
        ),
    ]
