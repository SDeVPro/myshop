<<<<<<< HEAD
# Generated by Django 3.0.8 on 2020-08-13 14:22
=======
# Generated by Django 3.0.8 on 2020-08-13 15:37
>>>>>>> origin/master

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0004_auto_20200809_1124'),
=======
        ('product', '0006_auto_20200810_2143'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
>>>>>>> origin/master
    ]

    operations = [
        migrations.CreateModel(
            name='ShopCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
