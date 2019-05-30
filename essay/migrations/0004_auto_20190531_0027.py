# Generated by Django 2.1.7 on 2019-05-30 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('essay', '0003_auto_20190531_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='essayanswer',
            name='answ',
            field=models.CharField(help_text='Enter the right answer', max_length=1000, verbose_name='CorrectAnswer'),
        ),
        migrations.AlterField(
            model_name='essayanswer',
            name='question',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='essay.Essay_Question', verbose_name='Question'),
        ),
    ]
