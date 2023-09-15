# Generated by Django 4.2 on 2023-04-28 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentinfo', '0002_courseinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnrollmentInfo',
            fields=[
                ('enrollmentid', models.IntegerField(primary_key=True, serialize=False)),
                ('courseid', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='studentinfo.courseinfo', verbose_name='course')),
                ('studentid', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='studentinfo.studentinfo', verbose_name='student')),
            ],
        )
    ]
