from django.contrib import admin
from .models import Emotional, Post

# Register your models here.
admin.site.register(Post)
admin.site.register(Emotional)