# Generated by Django 2.2 on 2020-03-15 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0003_questionnaire_is_dropdown'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='answer',
            field=models.BooleanField(default=False, help_text='Yes/No'),
        ),
    ]
