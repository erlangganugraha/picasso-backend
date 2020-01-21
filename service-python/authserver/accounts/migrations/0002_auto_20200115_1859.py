# Generated by Django 2.2.3 on 2020-01-15 11:59

from django.conf import settings
import django.contrib.postgres.indexes
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('auth', '0011_update_proxy_permissions'),
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nomoridentitaspengguna',
            name='jenis_identitas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.JenisNomorIdentitas', verbose_name='Jenis Nomor Identitas'),
        ),
        migrations.AddField(
            model_name='nomoridentitaspengguna',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='accounthistoryaction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='account',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accounts_account_create_by_user', to=settings.AUTH_USER_MODEL, verbose_name='Dibuat Oleh'),
        ),
        migrations.AddField(
            model_name='account',
            name='desa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.Desa', verbose_name='Desa'),
        ),
        migrations.AddField(
            model_name='account',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='account',
            name='rejected_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accounts_account_rejected_by_user', to=settings.AUTH_USER_MODEL, verbose_name='Dibatalkan Oleh'),
        ),
        migrations.AddField(
            model_name='account',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='account',
            name='verified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accounts_account_verify_by_user', to=settings.AUTH_USER_MODEL, verbose_name='Diverifikasi Oleh'),
        ),
        migrations.AddIndex(
            model_name='account',
            index=django.contrib.postgres.indexes.GinIndex(fields=['sv'], name='accounts_ac_sv_827d8f_gin'),
        ),
    ]
