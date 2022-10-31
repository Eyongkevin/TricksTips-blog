# Generated by Django 4.1 on 2022-10-26 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('blog', '0003_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_posts', to='category.category', verbose_name='Post Category'),
        ),
    ]
