# Generated by Django 2.0.5 on 2018-05-21 14:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('introduction', models.TextField(blank=True, null=True)),
                ('afterword', models.TextField(blank=True, null=True)),
                ('uuid', models.CharField(default=uuid.uuid4, editable=False, max_length=100)),
                ('length_minutes', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('profile_definition_json', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
