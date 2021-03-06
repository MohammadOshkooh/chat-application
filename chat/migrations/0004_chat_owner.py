# Generated by Django 4.0.6 on 2022-07-10 23:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0003_remove_chat_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner_set', to=settings.AUTH_USER_MODEL),
        ),
    ]
