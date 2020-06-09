# Generated by Django 3.0.5 on 2020-06-08 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_internshiphiddenfields'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='internship',
            options={'verbose_name': 'Staj', 'verbose_name_plural': 'Stajlar'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Öğrenci', 'verbose_name_plural': 'Öğrenciler'},
        ),
        migrations.AlterField(
            model_name='internshiphiddenfields',
            name='internship',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student'),
        ),
    ]