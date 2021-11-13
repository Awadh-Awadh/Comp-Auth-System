from django.contrib import admin
from django.db.models.fields import TextField
from .models import CustomUser, Profile


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

  #  formfield_overrides = {
  #    CustomUser.about: {'widget' : Textarea(attrs={'rows':10, 'cols': 40})}
  #  }
   add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )


admin.site.register(Profile)