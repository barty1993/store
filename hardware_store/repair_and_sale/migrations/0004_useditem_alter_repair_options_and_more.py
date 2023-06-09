# Generated by Django 4.2 on 2023-05-02 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair_and_sale', '0003_alter_repair_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsedItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('description', models.TextField(blank=True)),
                ('image_url', models.ImageField(upload_to='used_item/')),
            ],
            options={
                'verbose_name': 'б/у товар',
                'verbose_name_plural': 'б/у товары',
                'db_table': 'used_item',
            },
        ),
        migrations.AlterModelOptions(
            name='repair',
            options={'default_related_name': 'repairs', 'verbose_name': 'Услуга', 'verbose_name_plural': 'Услуги'},
        ),
        migrations.AlterModelOptions(
            name='repaircategory',
            options={'default_related_name': 'categories', 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории услуг'},
        ),
    ]
