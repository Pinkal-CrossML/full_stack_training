# Generated by Django 4.0.5 on 2022-06-23 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Process', '0004_cnn_model_alter_process_data_classification_model_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cnn_model',
            name='kernel_Initializer',
            field=models.CharField(choices=[('he_noraml', 'he_noraml'), ('he_uniform', 'he_uniform')], max_length=50, null=True),
        ),
    ]
