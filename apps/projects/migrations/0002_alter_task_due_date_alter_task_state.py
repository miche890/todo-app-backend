# Generated by Django 4.2.7 on 2023-11-26 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha de vencimiento'),
        ),
        migrations.AlterField(
            model_name='task',
            name='state',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projects.state', verbose_name='Estado'),
        ),
    ]