# Generated by Django 4.0.3 on 2022-03-31 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0008_student_contact_student_experience_student_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]