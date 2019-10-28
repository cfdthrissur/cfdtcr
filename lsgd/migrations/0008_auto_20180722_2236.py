# Generated by Django 2.0.6 on 2018-07-22 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lsgd', '0007_auto_20180722_2200'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assembly',
            fields=[
                ('assembly_code', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True)),
                ('assembly_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Parliament',
            fields=[
                ('parliament_code', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True)),
                ('parliament_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='lsgd',
            name='lsgd_assembly',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lsgd.Assembly'),
        ),
        migrations.AddField(
            model_name='lsgd',
            name='lsgd_parliament',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lsgd.Parliament'),
        ),
    ]