# Generated by Django 2.1.7 on 2020-03-04 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('law', '0002_lawcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='LawInnerCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('law', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='law.LawCategory')),
            ],
            options={
                'verbose_name_plural': 'Sub law category',
                'db_table': 'law_inner_category',
            },
        ),
    ]
