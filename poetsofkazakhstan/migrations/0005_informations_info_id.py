# Generated by Django 4.0.2 on 2022-02-21 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poetsofkazakhstan', '0004_remove_informations_info_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='informations',
            name='info_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='poetsofkazakhstan.poets'),
        ),
    ]
