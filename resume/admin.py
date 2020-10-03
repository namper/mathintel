from django.contrib import admin
from resume.models import Paper, Journal, Resume, University, Field

# @TODO: MODIFY ADMIN
admin.site.register([Paper, Journal, Resume, University, Field], )
