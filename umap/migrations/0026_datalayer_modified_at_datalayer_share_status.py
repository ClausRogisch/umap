# Generated by Django 5.1.4 on 2025-01-29 18:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("umap", "0025_alter_datalayer_geojson"),
    ]

    operations = [
        migrations.AddField(
            model_name="datalayer",
            name="modified_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="datalayer",
            name="share_status",
            field=models.SmallIntegerField(
                choices=[(0, "Inherit"), (99, "Deleted")],
                default=0,
                verbose_name="share status",
            ),
        ),
    ]
