# Generated by Django 4.2 on 2023-05-02 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0003_reviews_alter_category_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='staff_images')),
            ],
            options={
                'verbose_name_plural': 'Staff',
            },
        ),
    ]
