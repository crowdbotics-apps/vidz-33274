# Generated by Django 2.2.26 on 2022-02-01 17:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_load_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hall_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('url', models.URLField(blank=True, null=True)),
                ('youtube_id', models.CharField(blank=True, max_length=256, null=True)),
                ('hall', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='video_hall', to='home.Hall')),
            ],
        ),
    ]
