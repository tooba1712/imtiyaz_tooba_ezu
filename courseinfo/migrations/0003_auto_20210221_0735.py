# Generated by Django 3.1.6 on 2021-02-21 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseinfo', '0002_auto_20210221_0623'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instructor',
            options={'ordering': ['last_name', 'first_name', 'disambiguator']},
        ),
        migrations.AlterModelOptions(
            name='period',
            options={'ordering': ['period_sequence']},
        ),
        migrations.AlterModelOptions(
            name='registration',
            options={'ordering': ['section', 'student']},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ['course', 'section_name', 'semester']},
        ),
        migrations.AlterModelOptions(
            name='semester',
            options={'ordering': ['year__year', 'period__period_sequence']},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['last_name', 'first_name', 'disambiguator']},
        ),
        migrations.AlterModelOptions(
            name='year',
            options={'ordering': ['year']},
        ),
        migrations.AddConstraint(
            model_name='instructor',
            constraint=models.UniqueConstraint(fields=('last_name', 'first_name', 'disambiguator'), name='unique_instructor'),
        ),
        migrations.AddConstraint(
            model_name='registration',
            constraint=models.UniqueConstraint(fields=('section', 'student'), name='unique_registration'),
        ),
        migrations.AddConstraint(
            model_name='section',
            constraint=models.UniqueConstraint(fields=('semester', 'course', 'section_name'), name='unique_section'),
        ),
        migrations.AddConstraint(
            model_name='semester',
            constraint=models.UniqueConstraint(fields=('year', 'period'), name='unique_semester'),
        ),
        migrations.AddConstraint(
            model_name='student',
            constraint=models.UniqueConstraint(fields=('last_name', 'first_name', 'disambiguator'), name='unique_student'),
        ),
    ]
