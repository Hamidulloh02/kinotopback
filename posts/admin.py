from django.contrib import admin
from .models import Post,Category,Video
# Register your models here.
admin.site.register(Video)
admin.site.register(Category)
admin.site.register(Post)

# class PostAdmin(admin.ModelAdmin):
#     inlines = [PostImagesInline]
#     readonly_fields = ('updated_at', 'created_at')