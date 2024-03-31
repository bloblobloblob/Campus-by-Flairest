# Generated by Django 5.0 on 2024-01-11 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flairest_campus', '0003_institute_review_specialty_university_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialty',
            name='detail',
        ),
        migrations.RemoveField(
            model_name='specialty',
            name='info',
        ),
        migrations.AddField(
            model_name='specialty',
            name='city',
            field=models.CharField(default='город не указан', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialty',
            name='duration',
            field=models.CharField(default='не указано', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialty',
            name='ege',
            field=models.CharField(default='не указано', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialty',
            name='faculty',
            field=models.CharField(default='не указано', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialty',
            name='gos_or_private',
            field=models.CharField(default='не указано', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialty',
            name='language',
            field=models.CharField(default='не указано', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialty',
            name='level',
            field=models.CharField(default='не указано', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialty',
            name='links',
            field=models.CharField(default='не указано', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialty',
            name='max_students_number_free',
            field=models.CharField(default='не указано', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialty',
            name='max_students_number_paid',
            field=models.CharField(default='не указано', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialty',
            name='military_department',
            field=models.CharField(default='не указано', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialty',
            name='price',
            field=models.CharField(default='не указано', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialty',
            name='speciality_cod',
            field=models.CharField(default='не указано', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialty',
            name='study_form',
            field=models.CharField(default='не указано', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialty',
            name='university',
            field=models.CharField(default='не указано', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='university',
            name='features',
            field=models.CharField(default='не указано', max_length=2000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='specialty',
            name='about',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='discipline',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='special',
            field=models.CharField(max_length=2000),
        ),
    ]