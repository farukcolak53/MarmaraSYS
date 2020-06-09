# Generated by Django 3.0.5 on 2020-06-08 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_remove_internship_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='internship',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='student.Student'),
            preserve_default=False,
        ),
    ]