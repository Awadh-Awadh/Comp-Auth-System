from django.contrib import admin
from .models import CustomUser, Profile, Code


# Register your models here
@admin.register(CustomUser)
class UserAdminConfig(admin.ModelAdmin):
   search_field = ('email','username')
   ordering = ('-start_date',)
   list_filter = ('email', 'username', 'first_name', 'is_active', 'is_staff')
   list_display = ('email', 'username', 'first_name', 'is_active')
   fieldsets = (
       (None, {
           "fields": (
               'email', 'username', 'first_name'
           ),
       }),
       ('permissions', {
         "fields": ('is_staff','is_active')
       }),
       ("personal", {
         "fields": ('about',)
       }),
   )
   add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )


admin.site.register(Profile)
admin.site.register(Code)