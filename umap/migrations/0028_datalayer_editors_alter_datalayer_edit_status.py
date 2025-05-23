# Generated by Django 5.2.1 on 2025-05-17 08:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('umap', '0027_map_tags'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='datalayer',
            name='editors',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='editors'),
        ),
        migrations.AlterField(
            model_name='datalayer',
            name='edit_status',
            field=models.SmallIntegerField(choices=[(0, 'Inherit'), (1, 'Everyone'), (2, 'Editors and team only'), (4, 'Assigned Users and Owner'), (3, 'Owner only')], default=0, verbose_name='edit status'),
        ),
    ]
