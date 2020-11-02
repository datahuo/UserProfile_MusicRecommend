# Generated by Django 3.0.5 on 2020-04-16 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20200414_1715'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': '用户资料', 'verbose_name_plural': '用户资料'},
        ),
        migrations.AddField(
            model_name='userprofile',
            name='first_run',
            field=models.BooleanField(default=True, verbose_name='是否第一次运行 执行冷启动策略'),
        ),
    ]