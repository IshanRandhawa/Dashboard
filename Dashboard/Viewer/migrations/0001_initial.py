# Generated by Django 2.2.3 on 2019-07-13 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='L1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fsf_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='L2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fsf_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='L4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fsf_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='L3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fsf_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Viewer.L4')),
            ],
        ),
        migrations.CreateModel(
            name='L2_calls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Blconsumption', models.FloatField(default=0)),
                ('BlconsumptionT', models.IntegerField(default=0)),
                ('Coverage', models.IntegerField(default=0)),
                ('PNSconsumption', models.FloatField(default=0)),
                ('PNSconsumptionT', models.IntegerField(default=0)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Viewer.L2')),
            ],
        ),
        migrations.AddField(
            model_name='l2',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Viewer.L3'),
        ),
        migrations.CreateModel(
            name='L1_calls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Blconsumption', models.FloatField(default=0)),
                ('BlconsumptionT', models.IntegerField(default=0)),
                ('Coverage', models.IntegerField(default=0)),
                ('PNSconsumption', models.FloatField(default=0)),
                ('PNSconsumptionT', models.IntegerField(default=0)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Viewer.L1')),
            ],
        ),
        migrations.AddField(
            model_name='l1',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Viewer.L2'),
        ),
    ]