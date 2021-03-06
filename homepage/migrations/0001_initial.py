# Generated by Django 3.1.2 on 2020-10-02 21:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_boast', models.BooleanField()),
                ('post_text', models.CharField(max_length=200)),
                ('up_votes', models.IntegerField(default=0)),
                ('down_votes', models.IntegerField(default=0)),
                ('submission_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
    ]
