from django.contrib import admin
from .models import news, course, reviewer

admin.site.register(news)
admin.site.register(course)
admin.site.register(reviewer)