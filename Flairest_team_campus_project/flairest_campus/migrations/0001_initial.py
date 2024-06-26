# Generated by Django 5.0 on 2024-05-15 16:58

import django.db.models.deletion
import multiselectfield.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=300)),
                ('log_date', models.DateTimeField(verbose_name='date logged')),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(db_index=True, max_length=100)),
                ('speciality_cod', models.CharField(max_length=20)),
                ('ege', multiselectfield.db.fields.MultiSelectField(choices=[('Русский язык', 'Русский язык'), ('Математика', 'Математика'), ('Физика', 'Физика'), ('Химия', 'Химия'), ('История', 'История'), ('Обществознание', 'Обществознание'), ('Информатика', 'Информатика'), ('Биология', 'Биология'), ('География', 'География'), ('Иностранные языки', 'Иностранные языки'), ('Литература', 'Литература')], max_length=100)),
                ('photo', models.ImageField(upload_to='spec/')),
                ('about', models.TextField(max_length=1000)),
                ('special', models.TextField(max_length=2000)),
                ('city', models.CharField(choices=[('Екатеринбург', 'Екатеринбург'), ('Нижний Тагил', 'Нижний Тагил'), ('Каменск-Уральский', 'Каменск-Уральский'), ('Первоуральск', 'Первоуральск'), ('Серов', 'Серов'), ('Новоуральск', 'Новоуральск'), ('Верхняя Пышма', 'Верхняя Пышма'), ('Берёзовский', 'Берёзовский'), ('Ревда', 'Ревда'), ('Асбест', 'Асбест'), ('Краснотурьинск', 'Краснотурьинск')], default='Екатеринбург', max_length=40)),
                ('level', models.CharField(choices=[('Бакалавриат', 'Бакалавриат'), ('Специалитет', 'Специалитет'), ('Магистратура', 'Магистратура'), ('Аспирантура', 'Аспирантура')], default='Бакалавриат', max_length=40)),
                ('duration', models.CharField(choices=[('2 года', '2 года'), ('3 года', '3 года'), ('4 года', '4 года'), ('5 лет', '5 лет'), ('6 лет', '6 лет')], default='4 года', max_length=40)),
                ('study_form', multiselectfield.db.fields.MultiSelectField(choices=[('очная', 'очная'), ('очно-заочная', 'очно-заочная'), ('заочная', 'заочная')], max_length=50)),
                ('discipline', models.TextField(max_length=1000)),
                ('price', models.CharField(max_length=100)),
                ('passing_score_free', models.CharField(max_length=100)),
                ('max_students_number_free', models.CharField(max_length=100)),
                ('passing_score_paid', models.CharField(max_length=100)),
                ('max_students_number_paid', models.CharField(max_length=100)),
                ('links', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('photo', models.ImageField(upload_to='uni/')),
                ('about', models.TextField(max_length=2000)),
                ('features', models.TextField(max_length=2000)),
                ('contacts', models.TextField(max_length=300)),
                ('gorod', models.CharField(choices=[('Екатеринбург', 'Екатеринбург'), ('Нижний Тагил', 'Нижний Тагил'), ('Каменск-Уральский', 'Каменск-Уральский'), ('Первоуральск', 'Первоуральск'), ('Серов', 'Серов'), ('Новоуральск', 'Новоуральск'), ('Верхняя Пышма', 'Верхняя Пышма'), ('Берёзовский', 'Берёзовский'), ('Ревда', 'Ревда'), ('Асбест', 'Асбест'), ('Краснотурьинск', 'Краснотурьинск')], default='Екатеринбург', max_length=40)),
                ('military_department', models.CharField(choices=[('есть', 'есть'), ('нет', 'нет')], default='нет', max_length=40)),
                ('gos_or_private', models.CharField(choices=[('да', 'да'), ('нет', 'нет')], default='нет', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='NewUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.TextField(max_length=100)),
                ('review', models.TextField(max_length=1000)),
                ('date', models.CharField(default='15 Май 2024', editable=False)),
                ('specialty', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='flairest_campus.specialty')),
            ],
        ),
        migrations.AddField(
            model_name='specialty',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='flairest_campus.university'),
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='inst/')),
                ('about', models.CharField(max_length=1000)),
                ('special', models.CharField(max_length=1000)),
                ('contacts', models.CharField(max_length=300)),
                ('gorod', models.CharField(choices=[('Екатеринбург', 'Екатеринбург'), ('Нижний Тагил', 'Нижний Тагил'), ('Каменск-Уральский', 'Каменск-Уральский'), ('Первоуральск', 'Первоуральск'), ('Серов', 'Серов'), ('Новоуральск', 'Новоуральск'), ('Верхняя Пышма', 'Верхняя Пышма'), ('Берёзовский', 'Берёзовский'), ('Ревда', 'Ревда'), ('Асбест', 'Асбест'), ('Краснотурьинск', 'Краснотурьинск')], default='Екатеринбург', max_length=40)),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='flairest_campus.university')),
            ],
        ),
    ]
