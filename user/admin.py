from django.contrib import admin
from user.models import User, LegacyUser, Country

# @TODO: modify
admin.site.register([User, LegacyUser, Country], )
