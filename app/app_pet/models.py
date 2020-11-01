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

from django.views import View

class Departament(models.Model):
    name = models.CharField(max_length=50)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    class Meta:
        verbose_name = 'Департамент ЖКХ'
        verbose_name_plural = 'Департаменты ЖКХ'

class Prefecture(models.Model):
    name = models.CharField(max_length=50)
    departament = models.ForeignKey(Departament, on_delete=models.CASCADE, null=True)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    class Meta:
        verbose_name = 'Префектура'
        verbose_name_plural = 'Префектуры'

class Shelter(models.Model):
    name = models.CharField(max_length=50)
    prefecture = models.ForeignKey(Prefecture, on_delete=models.CASCADE,null=True)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    class Meta:
        verbose_name = 'Приют'
        verbose_name_plural = 'Приюты'

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
    class Meta:
        verbose_name = 'Управляющий'
        verbose_name_plural = 'Управляющие'


class MyUser(AbstractBaseUser):
    
    name = models.CharField(unique=True, max_length=100)
    Telegram = models.CharField( max_length=100,blank=True)
    mail = models.CharField(max_length=100,blank=True)
    phone = models.CharField(max_length=100,blank=True)

    pasport = models.CharField(max_length=100,blank=True)
    snils = models.CharField(max_length=100,blank=True)
    inn = models.CharField(max_length=100,blank=True)
    
    organization1 = models.CharField(blank=True, max_length=100)

    MANAGEER = "M"
    USER = "U"
    OWNERSHIP_CHOICES = [
        (MANAGEER, 'управление'),
        (USER, 'пользователь'),
    ]
    ownership = models.CharField(max_length=100, choices=OWNERSHIP_CHOICES ,blank=True) #пренадлежность пользователя
    
    natural_legal = models.CharField(max_length=100, choices=[('n','физическое'),('l','юридическое')]) #физическое или юридическое лицо
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
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
#####################################################################################################################################
#############################################                   МОДЕЛЬ ПИТОМЦА              #########################################
#####################################################################################################################################

class TypeVaccine(models.Model): #Вид вакцины
    name = models.CharField(max_length=30, unique=True, blank=False)
    class Meta:
        verbose_name = 'Вакцина'
        verbose_name_plural = 'Вакцины'

class PetModel(models.Model):
    DOG = 'd'
    CAT = 'c'
    TYPE_CHOICES = [
        (DOG, 'кошка'),
        (CAT, 'собака'),
    ]
    FOUND = 'f'
    LOST = 'l'
    FOUND_CHOICES = [
        (FOUND, 'found'),
        (LOST, 'lost'),
    ]
    
    MALE = 'm'
    FEMALE = 'f'
    SEX_CHOICES = [
        (MALE, 'мужской'),
        (FEMALE, 'женский'),
    ]

    BLACK = 'b'
    RED = 'r'
    WHITE = 'w'
    BLACK_WHITE = 'b-w'
    COLOR_CHOICE = [
        (BLACK, 'черный'),
        (WHITE, 'белый'),
        (BLACK_WHITE, 'черно-белый')
    ]

    SHORT = 's'
    LONG = 'l'
    NORMAL = 'n'
    COAT_CHOICE = [
        (SHORT, 'короткая'),
        (LONG, 'длинная'),
        (NORMAL, 'обычная')
    ]
    
    STANDING = 's'
    SEMI_STABLE = 's-s'
    HANGING = 'h'
    EARS_CHOICE = [
        (STANDING, 'стоячие'),
        (SEMI_STABLE, 'полустоячие'),
        (HANGING, 'висячие')
    ]

    CROCHET = 'c'
    SABER = 's'
    TAIL_CHOICE = [
        (NORMAL, 'обычный'),
        (CROCHET, 'крючком'),
        (SABER, 'саблевидный')
    ]
    
    BIG = 'b'
    SMALL = 's'
    MIDDLE = 'm'
    SIZE_CHOICE = [
        (BIG, 'большой'),
        (SMALL, 'маленький'),
        (MIDDLE, 'средний'),
    ]

    image = models.ImageField(upload_to="user_photo",blank = True,)


    card_pet = models.CharField(default="", max_length=15, unique=True, blank=False)                #карточка животного
    type_pet = models.CharField(default=DOG, choices=TYPE_CHOICES, max_length=1, blank=False)       #выбор типа животного
    age = models.IntegerField(blank=True)                                                           #возраст                           #
    weight = models.IntegerField(blank=True)                                                        #вес                                #
    nickname = models.CharField(default="", max_length=30, blank=True)                              #карточка животного
    sex = models.CharField(default="", max_length=30, choices=SEX_CHOICES, blank=False)             #пол животного
    breed_of_dog = models.CharField(default="", max_length=30, blank=True)                          #порода животного
    color = models.CharField(default="", blank=True, choices=COLOR_CHOICE, max_length=30)           # цвет животного
    fur = models.CharField(default="", blank=True, choices=COAT_CHOICE, max_length=30)              # шерсть
    ears = models.CharField(default="", blank=True, choices=EARS_CHOICE, max_length=30)             # уши
    tail = models.CharField(default="", blank=True, choices=TAIL_CHOICE, max_length=30)             # хвост
    size = models.CharField(default="", blank=True, choices=SIZE_CHOICE, max_length=30)             # размер
    special_signs = models.CharField(default="", blank=True, max_length=30)                         #особые приметы
    aviary_number = models.IntegerField(blank=True)                                                 #номер вольера                      #
    identification_mark = models.IntegerField (blank=True)                                          #идентификационная метка            #
    sterilization_date = models.CharField(default="", blank=True, max_length=30)                    #дата стерилизации
    veterinarian = models.CharField(default="", blank=True, max_length=30)                          # фио ветеринарного врача
    socialized = models.CharField(default="", blank=True, choices=[('y','да'), ('n','нет')], max_length=30) #социализировано
    act_work_order = models.CharField(default="", blank=True, max_length=30)                        #заказ-наряд акт
    data_work_order = models.CharField(default="", blank=True, max_length=30)                       #заказ-наряд дата
    capture_act = models.CharField(default="", blank=True, max_length=30)                           #акт отлова
    catching_address = models.CharField(default="", blank=True, max_length=30)                      #адрес отлова
    
    owner = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete=models.CASCADE, blank=True, null=True)       #сведения о новых владельцах        #
    
    date_admission = models.CharField(default="", blank=True, max_length=30)                        #дата поступления в приют
    act_admission = models.CharField(default="", blank=True, max_length=30)                         #акт поступления
    date_leaving = models.CharField(default="", blank=True, max_length=30)                          #дата выбытия
    date_leaving = models.CharField(default="", blank=True, max_length=30)                          #дата выбытия
    reason_leaving = models.CharField(default="", blank=True, max_length=30)                        #причина выбытия
    act_leaving = models.CharField(default="", blank=True, max_length=30)                           #акт выбытия



    shelter = models.ForeignKey(Shelter ,on_delete=models.CASCADE,blank=True, null=True)                      #информация по приюту

    typevaccine = models.ManyToManyField(TypeVaccine, blank=True, null=True)                          #сведения о вакцинации 


    date_inspection = models.CharField(default="", blank=True, max_length=30)                        #дата обследования
    anamnesis =models.CharField(default="", blank=True, max_length=30)                              #анамнез
    class Meta:
        verbose_name = 'Питомец'
        verbose_name_plural = 'Питомцы'

class Membership(models.Model):
    petmodel = models.ForeignKey(PetModel, on_delete=models.CASCADE)
    typevaccine = models.ForeignKey(TypeVaccine, on_delete=models.CASCADE)
    date_joined = models.DateField() #дата
    batch_number = models.CharField(max_length=64) #номер серии
    class Meta:
        verbose_name = 'Информация о вакцине'
        verbose_name_plural = 'Информации о вакцинах'
    
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
    
