# Generated by Django 4.1.4 on 2022-12-17 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('strategy', '0002_remove_strategy_product_and_more'),
        ('product', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competitor',
            name='product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='cuurent_discount_promo',
        ),
        migrations.AddField(
            model_name='product',
            name='current_discount_promo',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_article',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='strategy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_strategy', to='strategy.strategy'),
        ),
        migrations.CreateModel(
            name='CompetitorProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competitor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.competitor')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
