from django.db import models

# Create your models here.
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from django.shortcuts import reverse
from django.utils.text import slugify
from time import time

#################################################################################################################################
#########################################               МОДЕЛЬ ПОЛЬЗОВАТЕЛЯ             #########################################
#################################################################################################################################

class MyUserManager(BaseUserManager):
    def create_user(self, name, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not name:
            raise ValueError('Users must have an email address')

        user = self.model(
            name=name
        )
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            name,
            password=password,

        )

        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    name = models.CharField(unique=True, max_length=100)
    Telegram = models.CharField( max_length=100,blank=True)
    Vk = models.CharField( max_length=100,blank=True)
    phone = models.CharField(max_length=100,blank=True)
    shelter = models.BooleanField(default=False,blank=True)
    people = models.BooleanField(default=True,blank=True)
    avatar = models.ImageField(upload_to="user_photo",blank = True)
    SIMPLE = 's'
    MEDIUM = 'm'
    HARD = 'h'
    DONATE_CHOICES = [
        (SIMPLE, 'simple'),
        (MEDIUM, 'medium'),
        (HARD, 'hard'),
    ]
    donate = models.CharField(
        max_length=1,
        choices=DONATE_CHOICES,
        default=SIMPLE,blank=True
    )
    data_start_donat = models.DateField(blank=True, default="1994-04-23")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

#####################################################################################################################################
#############################################                   МОДЕЛЬ ПИТОМЦА              #########################################
#####################################################################################################################################

class PetModel(models.Model):
    DOG = 'd'
    CAT = 'c'
    OTHER = 'o'
    TYPE_CHOICES = [
        (DOG, 'dog'),
        (CAT, 'cat'),
        (OTHER, 'other'),
    ]
    FOUND = 'f'
    LOST = 'l'
    FOUND_CHOICES = [
        (FOUND, 'found'),
        (LOST, 'lost'),
    ]
    
    type_pet = models.CharField(default=DOG, choices=TYPE_CHOICES, max_length=1) #выбор типа животного
    sigma = models.BooleanField(default=False) #Клеймо
    found_lost = models.CharField(max_length=1, choices=FOUND_CHOICES, default=FOUND) #найден или потерялся
    data = models.DateTimeField() #Дата находки / потеряшки
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE) #ссылка на пользователя, который создал
    rewards = models.IntegerField() #Вознаграждение
    image1 = models.ImageField(upload_to="user_photo",blank = True,)
    image2 = models.ImageField(upload_to="user_photo",blank = True)
    image3 = models.ImageField(upload_to="user_photo",blank = True)
    image4 = models.ImageField(upload_to="user_photo",blank = True)
    description = models.TextField(max_length=1000, blank=True)


#####################################################################################################################################


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))

#####################################################################################################################################
#############################################                   МОДЕЛЬ ПОСТОВ              ##########################################
#####################################################################################################################################

class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True) # заголовок отзыва
    slug = models.SlugField(max_length=150, blank=True, unique=True) # уникальность
    body = models.TextField(blank=True,db_index=True) # тело отзыва
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts') # связанные теги
    date_pub = models.DateTimeField(auto_now_add=True) # дата публикации

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # для ссылок
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('post_update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('post_delete', kwargs={'slug': self.slug})


    def __str__(self):
        return self.title

#####################################################################################################################################
#############################################                   МОДЕЛЬ ТЕГОВ              ###########################################
#####################################################################################################################################

class Tag(models.Model):
    title = models.CharField(max_length=50) # заголовок тега
    slug = models.SlugField(max_length=50, unique=True)  # уникальность

    def  get_absolute_url(self):
        # для ссылок
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('tag_update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('tag_delete', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.title)
    