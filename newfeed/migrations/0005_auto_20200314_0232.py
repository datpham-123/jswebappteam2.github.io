# Generated by Django 3.0.3 on 2020-03-13 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newfeed', '0004_comment_1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_1',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_1s', to='newfeed.Post_Confession'),
        ),
    ]