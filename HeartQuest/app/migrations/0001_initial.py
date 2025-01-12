# Generated by Django 5.0.6 on 2024-06-12 16:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CentreInteret',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_dernier_message', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('prenom', models.CharField(max_length=200)),
                ('sexe', models.BooleanField(default=True)),
                ('date_naissance', models.DateField()),
                ('lieu_naissance', models.CharField(max_length=200)),
                ('bio', models.TextField(default='Biographie')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=200)),
                ('date_enregistrement', models.DateField(auto_now_add=True)),
                ('profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profil')),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texte', models.TextField(null=True)),
                ('image', models.ImageField(null=True, upload_to='images/Publications/')),
                ('video', models.FileField(null=True, upload_to='videos/Publications/')),
                ('date_ajout', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoUtilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='images/Utilisateur/')),
                ('date_ajout', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texte', models.TextField(null=True)),
                ('image', models.ImageField(null=True, upload_to='images/Messages/')),
                ('video', models.FileField(null=True, upload_to='videos/Messages/')),
                ('document', models.FileField(null=True, upload_to='documents/Messages/')),
                ('audio', models.FileField(null=True, upload_to='audios/Messages/')),
                ('date_envoi', models.DateTimeField(auto_now_add=True)),
                ('conversation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.conversation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
        migrations.AddField(
            model_name='conversation',
            name='user1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user1', to='app.user'),
        ),
        migrations.AddField(
            model_name='conversation',
            name='user2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user2', to='app.user'),
        ),
        migrations.CreateModel(
            name='CentreInteretUtilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('centre_interet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.centreinteret')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
    ]
