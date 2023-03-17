from django.db import models

# Create your models here.




Choices_for_Gender =(("1", "Male"),("2", "Female"),("3", "Other"),)
Choices_for_status=("pending","completed")

class User(models.Model):
    Phone_number=models.IntegerField(unique=True)
    email_id=models.EmailField(max_length=80)
    is_customer=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.email_id


class Profile(models.Model):
    owner=models.OneToOneField(User)
    name=models.CharField(max_length=100)
    date_of_birth=models.DateField()
    gender=models.ChoicesField(choices=Choices_for_Gender)
    image= models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)


class Login(models.Model):
    owner=models.ForeignKey(User)
    product=models.ForeignKey(Product)
    status=models.Choices(choices=Choices_for_status)
    
    
class CartProduct(models.Model):
    owner=models.ForeignKey(User)
    product=models.ForeignKey(Product)
    status=models.Choices(choices=Choices_for_status)
    
class Cart(models.Model):
    owner=models.ForeignKey(User)
    product=models.ManyToManyField(CartProduct)
    price=models.IntegerField()
    