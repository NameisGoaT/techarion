from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Login)
admin.site.register(CartProduct)
admin.site.register(Cart)

# Register your models here.
