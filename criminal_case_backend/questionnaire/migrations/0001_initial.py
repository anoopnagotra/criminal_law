# Generated by Django 2.2 on 2020-03-15 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('ques_type', models.CharField(choices=[('accused', 'accused'), ('victim', 'victim'), ('offence', 'offence')], help_text='Questionnaire Type', max_length=120)),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Questionnaire',
                'db_table': 'questionnaires',
            },
        ),
    ]
