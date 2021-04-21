from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import UserAuth

admin.site.register(UserAuth, UserAdmin)
