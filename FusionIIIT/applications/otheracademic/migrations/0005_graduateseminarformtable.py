# Generated by Django 3.1.5 on 2024-02-20 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otheracademic', '0004_auto_20240220_0947'),
    ]

    operations = [
        migrations.CreateModel(
            name='GraduateSeminarFormTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.CharField(max_length=20)),
                ('semester', models.CharField(max_length=100)),
                ('date_of_seminar', models.DateField()),
            ],
            options={
                'db_table': 'GraduateSeminarFormTable',
            },
        ),
    ]
