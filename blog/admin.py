from django.contrib import admin
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.utils.safestring  import mark_safe
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    save_as=True
    save_on_top=True
    list_display=('id','title','created_at','get_photo')
    list_display_links=('id','title','created_at','get_photo')
    search_fields=('title',)
    #list_filter=('category','tags',)
    readonly_fields=('views','created_at','get_photo')
    fields=('title','slug','category','content','photo','get_photo','created_at','views','teacher','fee','seat','duration')
    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'
    get_photo.short_description="Фото"


class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    save_as=True
    save_on_top=True
    list_display=('id','title','created_at','get_photo')
    list_display_links=('id','title','created_at','get_photo')
    search_fields=('title',)
    #list_filter=('category','tags',)
    readonly_fields=('views','created_at','get_photo')
    fields=('title','slug','content','photo','get_photo','created_at','views')
    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'
    get_photo.short_description="Фото"
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id','title','created_at')

class AboutAdmin(admin.ModelAdmin):
    list_display = ('id','title','created_at','photo')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id','title','created_at','photo')
admin.site.register(Post,PostAdmin)
admin.site.register(News,NewsAdmin)
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(About,AboutAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Feedback,FeedbackAdmin)