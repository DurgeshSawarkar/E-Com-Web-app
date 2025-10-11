from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.forms import ValidationError
# Create your models here.

#creating user from this model
class MyAccountManager(BaseUserManager):
   
   def create_user(self, first_name, last_name, username, email, password = None ):
      if not email:
        raise ValidationError("Enter a valid email address.")

      if not username:
         raise ValidationError("Please enter user name")


      user = self.model(
         email = self.normalize_email(email),
         username = username,
         first_name =first_name,
         last_name =last_name,
      ) 

      user.set_password(password)
      user.save(using=self._db)
      return user


   #create superuser from this model
   def create_superuser(self, first_name, last_name, username, email, password = None ):
      user =self.create_user(
        email = self.normalize_email(email),
        username = username,
        first_name =first_name,
        last_name =last_name,
        password=password,
      )
      user.is_admin  = True
      user.is_staff  = True
      user.is_active  = True
      user.is_superadmin  = True 
      user.save(using=self._db)







# user model
class Account(AbstractBaseUser):
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)

    #required 
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login =models.DateTimeField(auto_now_add=True)
    is_admin  = models.BooleanField(default=False)
    is_staff  = models.BooleanField(default=False)
    is_active  = models.BooleanField(default=False)
    is_superadmin  = models.BooleanField(default=False)

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = MyAccountManager()

    class Meta:
        verbose_name = ("Account")
        verbose_name_plural = ("Accounts")

    def __str__(self):
        return self.email

    def has_perm(self, prem, obj=None):
     return self.is_admin

    def has_module_perms(self, add_lable):
       return True