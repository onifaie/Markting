# Generated by Django 3.2.4 on 2021-06-25 06:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={},
        ),
        migrations.AddField(
            model_name='product',
            name='Test',
            field=models.ForeignKey(default=1, max_length=100, on_delete=django.db.models.deletion.CASCADE, to='product.test'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='create_dt',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='proname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
