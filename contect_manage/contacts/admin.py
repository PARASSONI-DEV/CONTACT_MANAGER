from django.contrib import admin
from .models import User,Profile,contects


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=['username','email']

class ProfileAdmin(admin.ModelAdmin):
    list_display=['verified']
    list_display=['user','fullname','number']

class ContectsAdmin(admin.ModelAdmin):
    list_display=['name','number','address','completed']


admin.site.register(User,UserAdmin)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(contects,ContectsAdmin)


