# Generated by Django 5.2.1 on 2025-06-06 09:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workdesk', '0003_alter_workdeskmembership_workdeskname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workdeskmembership',
            name='workdeskName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='workdesk.workdesk'),
        ),
    ]
