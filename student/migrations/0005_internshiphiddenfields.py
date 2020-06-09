# Generated by Django 3.0.5 on 2020-06-08 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_internship_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternShipHiddenFields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internshipDevamNotu', models.IntegerField(verbose_name='Staj Devam Notu')),
                ('internshipCalismaNotu', models.IntegerField(verbose_name='Çalışma Ve Gayret Notu')),
                ('internshipZamanNotu', models.IntegerField(verbose_name='İşi Zamanında ve Tam Yapma Notu')),
                ('internshipAmirNotu', models.IntegerField(verbose_name='Amirine Karşı Tutumu Notu')),
                ('internshipArkadas', models.IntegerField(verbose_name='İşçi ve Arkadaşlarına Karşı Tutumu Notu')),
                ('internshipDiger', models.ImageField(upload_to='uploads/', verbose_name='Değerlendirme Formu')),
                ('firmaDegerlendirme', models.BooleanField(verbose_name='Firma Değerlendirme')),
                ('firmaYorumu', models.TextField(verbose_name='Firma Yorumu')),
                ('internship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.InternShip')),
            ],
        ),
    ]