# Generated by Django 2.2 on 2020-03-18 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0007_auto_20200318_1718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionnaire',
            name='answer',
        ),
        migrations.AlterField(
            model_name='quesanswer',
            name='ques',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionnaire.Questionnaire', unique=True),
        ),
    ]
