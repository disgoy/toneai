# Generated by Django 5.1.2 on 2024-10-20 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Texts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_input', models.TextField()),
                ('classification', models.TextField()),
                ('text_response', models.TextField()),
                ('created_at', models.DateTimeField()),
            ],
        ),
    ]
