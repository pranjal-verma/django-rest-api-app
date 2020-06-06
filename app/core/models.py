from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin, \
                                                        AbstractBaseUser

class UserManager(BaseUserManager):


    def create_user(self, email, password = None, **exceptions):
        """ Create user by emailid and password """
        if not email:
            raise ValueError('Email is necessary')
        #email = email.lower()
        user = self.model(email =self.normalize_email(email), **exceptions)
        user.set_password(password)
        user.save(using = self._db)

        return user
    def create_superuser(self, email, password):
        """ Create new super user """
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True

        user.save(using = self._db)

        return user

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    """ Custom user model that supports using email instead of username """

    email = models.EmailField(max_length = 255, unique = True)
    name = models.CharField(max_length = 255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    
    USERNAME_FIELD = 'email'

