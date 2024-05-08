# Generated by Django 5.0.1 on 2024-05-07 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('courses', models.ManyToManyField(related_name='students', to='manytomany_app.course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='students_related',
            field=models.ManyToManyField(related_name='courses_related', to='manytomany_app.student'),
        ),
    ]