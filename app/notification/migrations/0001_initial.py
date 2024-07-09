# Generated by Django 5.0.6 on 2024-07-09 15:52

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('updated_at', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
                'db_table': 'contacts',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('updated_at', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('failed', 'Failed'), ('success', 'Success')], default='pending', max_length=10)),
                ('channel', models.CharField(choices=[('EMAIL', 'Email'), ('SMS', 'Sms'), ('WHATSAPP', 'Whatsapp')], max_length=10)),
                ('message', models.TextField()),
                ('execution_date', models.DateTimeField()),
                ('start_date', models.DateField(default=None, null=True)),
                ('end_date', models.DateField(default=None, null=True)),
                ('type_task', models.CharField(choices=[('periodic', 'Periodic'), ('schedule', 'Schedule')], max_length=10)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notification.contact')),
            ],
            options={
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
                'db_table': 'notifications',
            },
        ),
    ]