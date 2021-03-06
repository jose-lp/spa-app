# Generated by Django 3.1.2 on 2020-11-14 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='service',
            field=models.CharField(choices=[('Massage', 'Massage'), ('Manicure', 'Manicure'), ('Pedicure', 'Pedicure'), ('Facial Cleansing', 'Facial Cleansing'), ('Permanent Hair Removal', 'Permanent Hair Removal'), ('Cryotherapy', 'Cryotherapy')], max_length=25),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.CharField(choices=[('8:00 AM', '8:00 AM'), ('9:00 AM', '9:00 AM'), ('10:00 AM', '10:00 AM'), ('11:00 AM', '11:00 AM'), ('1:00 PM', '1:00 PM'), ('2:00 PM', '2:00 PM'), ('3:00 PM', '3:00 PM'), ('4:00 PM', '4:00 PM')], max_length=10),
        ),
    ]
