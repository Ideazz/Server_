from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from picklefield.fields import PickledObjectField
#from django.contrib.postgres.fields import ArrayField


class CustomUser(AbstractUser):
      name = models.CharField(blank=True, max_length=255)
      is_ideator = models.BooleanField(default=True)
      is_entrepreneur=models.BooleanField(default=False)
      city=models.CharField(blank=True,max_length=20)
      date_of_birth = models.DateField(max_length=8,blank=True,null=True)


class Ideator(models.Model):
     user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
     username=models.CharField(max_length=50,blank=True)
     city=models.CharField(blank=True,max_length=200)
     state=models.CharField(blank=True,max_length=300)
     country=models.CharField(blank=True,max_length=300)
     description=models.CharField(blank=True,max_length=500)
     current_occupation=models.CharField(blank=True,max_length=300)
     date_of_birth = models.DateField(max_length=8,blank=True,null=True)
     #skills = ArrayField(models.CharField(max_length=200), blank=True)


     def __str__(self):
         return self.username

     def create_user(sender , instance, **kwargs):
           if(instance.is_ideator==True):
                student_profile=Ideator.objects.create(user=instance,username=instance.username,date_of_birth=instance.date_joined)
     post_save.connect(create_user,sender=CustomUser)

class Entrepreneur(models.Model):
     user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
     username=models.CharField(max_length=20,blank=True)
     city=models.CharField(blank=True,max_length=200)
     state=models.CharField(blank=True,max_length=300)
     country=models.CharField(blank=True,max_length=300)
     description=models.CharField(blank=True,max_length=500)
     current_occupation=models.CharField(blank=True,max_length=300)
     date_of_birth = models.DateField(max_length=8,blank=True,null=True)
     refral_created=models.CharField(max_length=6,blank=True)
     refral_accessed=models.CharField(max_length=6,blank=True)
     Is_investor=models.BooleanField(default=False)


     def __str__(self):
         return self.username

     def create_user(sender , instance, **kwargs):
              if(instance.is_entrepreneur==True):
                   entrepreneur_profile=Entrepreneur.objects.create(user=instance,username=instance.username)
     post_save.connect(create_user,sender=CustomUser)




class Refral_directory(models.Model):
    args=PickledObjectField()

    #def push_dictionary(sender,instance,**kwargs):
    #      if (instance.refral_accessed == None):
        #      print("none")
        #  else:
        #      jack= entrepreneur.objects.get(refral_created=instance.refral_accessed)
         # print(instance.refral_accessed + jack.username)
         # push_directory=refral_directory(args={instance.refral_accessed : jack.username})
    #post_save.connect(push_dictionary,sender=Entrepreneur)
