# Generated by Django 4.1.2 on 2022-11-28 10:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pathlib


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_name', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to=pathlib.PurePosixPath('/home/adnan/Ecommerce/media'))),
                ('offer', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(max_length=255)),
                ('discount_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('trending', models.BooleanField(default=False)),
                ('Slider', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.company')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSpecification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.CharField(max_length=255)),
                ('weight_dimensions', models.CharField(max_length=255)),
                ('display', models.CharField(max_length=255)),
                ('chip', models.CharField(max_length=255)),
                ('camera', models.CharField(max_length=255)),
                ('video_recording', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=250)),
                ('review', models.TextField(blank=True)),
                ('rating', models.IntegerField(default=1)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_img', models.ImageField(blank=True, null=True, upload_to=pathlib.PurePosixPath('/home/adnan/Ecommerce/media'))),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='specification',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productspecification'),
        ),
        migrations.CreateModel(
            name='CheckoutCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
