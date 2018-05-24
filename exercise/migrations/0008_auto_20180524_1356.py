# Generated by Django 2.0.5 on 2018-05-24 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0007_auto_20180524_1341'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exerciseemail',
            old_name='email_from',
            new_name='email_from_email',
        ),
        migrations.AddField(
            model_name='exerciseemail',
            name='email_from_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]