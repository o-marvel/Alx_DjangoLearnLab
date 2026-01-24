# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import CustomUser

# class CustomUserAdmin(UserAdmin):
#     model = CustomUser

#     fieldsets = UserAdmin.fieldsets + (
#         ("Additional Info", {
#             "fields": ("date_of_birth", "profile_photo"),
#         }),
#     )

#     add_fieldsets = UserAdmin.add_fieldsets + (
#         ("Additional Info", {
#             "fields": ("date_of_birth", "profile_photo"),
#         }),
#     )
    
# # admin.site.register(CustomUser, CustomUserAdmin)
# # Register your models here.




# @admin.register(CustomUser)
# class CustomUserAdmin(UserAdmin):
#     fieldsets = UserAdmin.fieldsets + (
#         ("Additional Info", {
#             "fields": ("date_of_birth", "profile_photo"),
#         }),
#     )

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """
    Admin configuration for CustomUser.
    Ensures new fields appear in Django admin.
    """

    fieldsets = UserAdmin.fieldsets + (
        ("Additional Information", {
            "fields": ("date_of_birth", "profile_photo"),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Information", {
            "fields": ("date_of_birth", "profile_photo"),
        }),
    )

    list_display = ("username", "email", "is_staff", "is_active")
