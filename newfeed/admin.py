from django.contrib import admin
from .models import Post,Sent_Confession, Post_Confession,Comment_1

# Register your models here.
admin.site.register(Post)
admin.site.register(Sent_Confession)
admin.site.register(Post_Confession)