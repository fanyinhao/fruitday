# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-04 01:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userinfo', '0001_initial'),
        ('memberapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ccount', models.IntegerField(db_column='cart_count', verbose_name='数量')),
                ('good', models.ForeignKey(db_column='good_id', on_delete=django.db.models.deletion.CASCADE, to='memberapp.Goods')),
                ('user', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='userinfo.UserInfo')),
            ],
            options={
                'db_table': 'cartinfo',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderNo', models.CharField(max_length=200, verbose_name='订单号')),
                ('ads', models.CharField(max_length=200, verbose_name='收件人')),
                ('acot', models.CharField(max_length=200, verbose_name='总数')),
                ('acounts', models.CharField(max_length=200, verbose_name='价格')),
                ('cals', models.TextField(blank=True, null=True, verbose_name='orderdetail')),
                ('orderStatus', models.IntegerField(blank=True, choices=[(1, '未支付'), (2, '已支付'), (3, '订单取消')], default='1', verbose_name='订单状态')),
                ('user', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='userinfo.UserInfo')),
            ],
        ),
    ]
