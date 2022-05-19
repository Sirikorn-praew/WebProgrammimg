# Generated by Django 4.0.2 on 2022-05-18 12:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('checkbox', models.BooleanField(default=False)),
                ('duedate', models.DateTimeField(default='2022-05-18 12:21:43')),
                ('created_at', models.DateTimeField(default='2022-05-18 12:21:43')),
                ('involved', models.ManyToManyField(related_name='Involved', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
