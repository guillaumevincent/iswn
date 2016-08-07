import uuid
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db.models.signals import post_save


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password, )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    first_name = models.CharField(verbose_name='first name', max_length=30, blank=True)
    last_name = models.CharField(verbose_name='last name', max_length=30, blank=True)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"


class DateMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name='created')
    modified = models.DateTimeField(auto_now=True, verbose_name='modified')

    class Meta:
        abstract = True


class Chateau(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return '%s' % self.nom

    class Meta:
        verbose_name = "Chateau"
        verbose_name_plural = "Chateaux"


class Millesime(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    millesime = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return '%d' % self.millesime

    class Meta:
        verbose_name = "Millesime"
        verbose_name_plural = "Millesimes"


class Appellation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return '%s' % self.nom

    class Meta:
        verbose_name = "Appellation"
        verbose_name_plural = "Appellations"


class Classement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return '%s' % self.nom

    class Meta:
        verbose_name = "Classement"
        verbose_name_plural = "Classements"


class Couleur(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return '%s' % self.nom

    class Meta:
        verbose_name = "Couleur"
        verbose_name_plural = "Couleurs"


class ISWN(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    iswn = models.CharField(max_length=255, unique=True, null=True, blank=True)
    chateau = models.ForeignKey(Chateau, on_delete=models.SET_NULL, null=True, blank=True)
    millesime = models.ForeignKey(Millesime, on_delete=models.SET_NULL, null=True, blank=True)
    appellation = models.ForeignKey(Appellation, on_delete=models.SET_NULL, null=True, blank=True)
    classement = models.ForeignKey(Classement, on_delete=models.SET_NULL, null=True, blank=True)
    couleur = models.ForeignKey(Couleur, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "ISWN"
        verbose_name_plural = "ISWN"

    def __str__(self):
        return '%s' % self.id
