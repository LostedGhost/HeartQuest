from django.db import models

# Create your models here.
class Profil(models.Model):
    libelle = models.CharField(max_length = 200)

class User(models.Model):
    nom = models.CharField(max_length = 200)
    prenom = models.CharField(max_length = 200)
    sexe = models.BooleanField(default=True) # True pour les garçons, False pour les filles
    date_naissance = models.DateField()
    lieu_naissance = models.CharField(max_length = 200)
    bio = models.TextField(default="Biographie")
    email = models.EmailField()
    password = models.CharField(max_length = 200)
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    date_enregistrement = models.DateField(auto_now_add=True)

class PhotoUtilisateur(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/Utilisateur/')
    date_ajout = models.DateTimeField(auto_now_add=True)

class CentreInteret(models.Model):
    libelle = models.CharField(max_length = 200)

class CentreInteretUtilisateur(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    centre_interet = models.ForeignKey(CentreInteret, on_delete=models.CASCADE)

class Conversation(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user1")
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user2")
    date_creation = models.DateTimeField(auto_now_add=True)
    date_dernier_message = models.DateTimeField(null=True)
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    texte = models.TextField(null=True)
    image = models.ImageField(upload_to='images/Messages/', null=True)
    video = models.FileField(upload_to='videos/Messages/', null=True)
    document = models.FileField(upload_to='documents/Messages/',null=True)
    audio = models.FileField(upload_to='audios/Messages/', null=True)
    date_envoi = models.DateTimeField(auto_now_add=True)

class Publication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    texte = models.TextField(null=True)
    image = models.ImageField(upload_to='images/Publications/', null=True)
    video = models.FileField(upload_to='videos/Publications/', null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)