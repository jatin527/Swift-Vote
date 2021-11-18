# Generated by Django 3.0.5 on 2021-11-18 05:51

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='userDetails',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, verbose_name='email_address')),
                ('fName', models.CharField(max_length=30)),
                ('lName', models.CharField(max_length=30)),
                ('contactNumber', models.CharField(max_length=10)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('DOB', models.DateField()),
                ('documentLocation', models.CharField(blank=True, max_length=500, null=True)),
                ('Address', models.TextField()),
                ('type', models.CharField(choices=[('official', 'Official'), ('Voter', 'Voter'), ('Candidate', 'Candidate')], max_length=20)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='candidates',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('party', models.CharField(max_length=60)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='election',
            fields=[
                ('eid', models.AutoField(primary_key=True, serialize=False)),
                ('electionType', models.CharField(max_length=250)),
                ('allowedContext', models.CharField(max_length=250)),
                ('voteCount', models.BigIntegerField()),
                ('sDate', models.DateTimeField()),
                ('fDate', models.DateTimeField()),
                ('inCharge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='location',
            fields=[
                ('lid', models.AutoField(primary_key=True, serialize=False)),
                ('context', models.CharField(max_length=20)),
                ('locationName', models.CharField(max_length=500)),
                ('locationVoteCount', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.election')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='userVerification',
            fields=[
                ('vid', models.AutoField(primary_key=True, serialize=False)),
                ('documentType', models.CharField(max_length=50)),
                ('documentName', models.CharField(max_length=50)),
                ('Status', models.BooleanField()),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.candidates')),
            ],
        ),
        migrations.CreateModel(
            name='candidateHistory',
            fields=[
                ('hid', models.AutoField(primary_key=True, serialize=False)),
                ('voteCount', models.BigIntegerField()),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.candidates')),
                ('election', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.election')),
            ],
        ),
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('aid', models.AutoField(primary_key=True, serialize=False)),
                ('accountType', models.CharField(choices=[('official', 'Official'), ('normie', 'Normie')], max_length=20)),
                ('accountString', models.CharField(max_length=250)),
                ('accountPrivate', models.TextField()),
                ('accountPublic', models.TextField()),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]