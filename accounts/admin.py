from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts import models as user_models

admin.site.register(user_models.ProjectUser, UserAdmin)
admin.site.register(user_models.Admin)
admin.site.register(user_models.Employee)
