from django.contrib import admin
from users.models import User, Favorite

admin.site.register(User)
admin.site.register(Favorite)