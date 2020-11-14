# Generated by Django 3.1.2 on 2020-11-12 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type_user', models.CharField(choices=[('Admin', 'A'), ('Normal', 'N')], max_length=7)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('Male', 'M'), ('Female', 'F'), ('Other', 'O')], max_length=6)),
                ('age', models.PositiveIntegerField(blank=True)),
                ('telephone', models.PositiveIntegerField(blank=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estetician', models.CharField(choices=[('José López', 'JL'), ('Mariela Hernández', 'MH')], max_length=25)),
                ('service', models.CharField(choices=[('Massage', '0'), ('Manicure', '1'), ('Pedicure', '2'), ('Facial Cleansing', '3'), ('Permanent Hair Removal', '4'), ('Cryotherapy', '5')], max_length=25)),
                ('date', models.DateField()),
                ('time', models.CharField(choices=[('8:00 AM', '8:00'), ('9:00 AM', '9:00'), ('10:00 AM', '10:00'), ('11:00 AM', '11:00'), ('1:00 PM', '13:00'), ('2:00 PM', '14:00'), ('3:00 PM', '15:00'), ('4:00 PM', '16:00')], max_length=10)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.user')),
            ],
        ),
    ]
