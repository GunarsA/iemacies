# Generated by Django 5.0 on 2024-01-02 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_application_status_alter_lesson_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('ONGOING', 'Ongoing'), ('FINISHED', 'Finished')], default='PENDING', max_length=10),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='status',
            field=models.CharField(choices=[('UPCOMING', 'Upcoming'), ('FINISHED', 'Finished')], default='UPCOMING', max_length=10),
        ),
    ]
