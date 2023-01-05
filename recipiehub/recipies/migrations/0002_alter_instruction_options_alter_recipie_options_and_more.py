# Generated by Django 4.1.4 on 2022-12-28 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instruction',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='recipie',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='instruction',
            name='order',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='recipie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='recipies.recipie'),
        ),
        migrations.AlterField(
            model_name='instruction',
            name='recipie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instructions', to='recipies.recipie'),
        ),
    ]