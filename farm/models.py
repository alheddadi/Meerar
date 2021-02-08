from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

# Create your models here.

class magaalada(models.Model):
    name = models.CharField(max_length=200, null=True)
    lon = models.CharField(max_length=200, null=True)
    lat = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name
class gobolka(models.Model):
    name = models.CharField(max_length=200, null=True)
    lon = models.CharField(max_length=200, null=True)
    lat = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name




class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        return User.objects.create_user(email, password=password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=False.')

        return self._create_user(email, password, **extra_fields) 

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField( unique=True)
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=200, null=True)
    Number = models.CharField(max_length=200, null=True)
    user_pic = models.ImageField(blank=True,default = '../../static/img/farmer.png')

    gobolka = models.ForeignKey(gobolka, null=True, on_delete= models.SET_NULL)
    magaalada = models.ForeignKey(magaalada, null=True, on_delete= models.SET_NULL)

    date_joined = models.DateTimeField( auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField( default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)





class Product(models.Model):
    name = models.CharField(max_length=200)
    product_pic = models.ImageField(blank=True,default = '../../static/img/somfarm.jpg')
    amount = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)
    User = models.ForeignKey(User, null=True,blank=True, on_delete= models.SET_NULL)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class pricess(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)
    created_on = models.DateField(auto_now_add=True)

class Cars(models.Model):
    car_type = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)
    info = models.CharField(max_length=200)
    number = models.CharField(max_length=200)


    product_pic = models.ImageField(blank=True,default = '../../static/img/gaadhi.jpg')

class Reports(models.Model):
    Product = models.ForeignKey(Product, null=True,blank=True, on_delete= models.SET_NULL)
    amount = models.IntegerField()
    price = models.IntegerField()
    total = models.IntegerField(null=True,blank=True)
    Date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
      total = self.amount * self.price
      super(Reports, self).save(*args, **kwargs)

    