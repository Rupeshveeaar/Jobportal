# Generated by Django 4.0.3 on 2022-03-30 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0005_remove_company_company_pic_remove_company_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='demo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('demo', models.CharField(max_length=55)),
            ],
        ),
    ]