# Generated by Django 5.0 on 2024-01-02 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_remove_webbranch_is_cursor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectcategory',
            name='web_branches',
        ),
        migrations.DeleteModel(
            name='WebBranch',
        ),
    ]
