# Generated by Django 3.2.4 on 2022-08-12 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_alter_task_student_support_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='batches',
            field=models.CharField(choices=[('n/a', 'N/A'), ('batch1', 'Batch1'), ('batch2', 'Batch2'), ('batch3', 'Batch3'), ('batch4', 'Batch4'), ('batch5', 'Batch5'), ('under_training', 'Under Training')], default='n/a', max_length=50, verbose_name='Batch'),
        ),
        migrations.AddField(
            model_name='task',
            name='shifts',
            field=models.CharField(choices=[('n/a', 'N/A'), ('day', 'Day'), ('night', 'Night'), ('afternoon', 'Afternoon')], default='n/a', max_length=50, verbose_name='Shifts'),
        ),
    ]