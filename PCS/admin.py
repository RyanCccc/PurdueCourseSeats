from django.contrib import admin
from django.contrib.auth.models import User as Auth_User

# Add Users to admin site
admin.site.register(Auth_User)
