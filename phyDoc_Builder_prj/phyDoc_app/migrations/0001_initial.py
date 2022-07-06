# Generated by Django 4.0.1 on 2022-07-06 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document_templates',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('Document_template_path', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Document_details',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('field_name', models.CharField(max_length=80)),
                ('field_type', models.CharField(max_length=80)),
                ('isRequired', models.BooleanField(default=False)),
                ('templateid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phyDoc_app.document_templates')),
            ],
        ),
    ]
