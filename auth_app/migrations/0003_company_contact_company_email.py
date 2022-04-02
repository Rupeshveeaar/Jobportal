# Generated by Django 4.0.3 on 2022-03-29 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0002_remove_company_email_remove_company_job_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='contact',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='email',
            field=models.EmailField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]