from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.db.models.signals import post_save
# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self,first_name,last_name,username,email,password=None):
        if not email:
            raise ValueError('User Must Have AN Email Address')
        if not username:
            raise ValueError('User Must Have An username')
        
        User=self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            username=username,
            
        )
        User.set_password(password)
        User.save(using=self._db)
        return User
    
    def create_superuser(self,first_name,last_name,username,email,password=None):
        User=self.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=self.normalize_email(email),
            password=password,
        )
        User.is_admin=True
        User.is_active=True
        User.is_staff=True
        User.is_superadmin=True
        User.save(using=self.db)
        return User




class User(AbstractBaseUser,):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,unique=True)
    is_admin=False
    is_active=True
    is_staff=False
    is_superadmin=False
    
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

    objects=UserManager()

    def __str__(self) :
        return self.email
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,app_label):
        return True
    

    def profile(self):
        profile = Profile.objects.get(user=self)



class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    fullname=models.CharField(max_length=100)
    number=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    verified=models.BooleanField(default=False)


def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)



def save_user_profile(sender,instance,**kwargs):
    instance.Profile.save()

post_save.connect(create_user_profile,sender=User)
post_save.connect(create_user_profile,sender=User)



class contects(models.Model):
    name=models.CharField(max_length=250)
    address=models.CharField(max_length=250)
    number=models.CharField(max_length=250)
    completed=models.BooleanField(default=False)


    def __str__(self):
        return self.name