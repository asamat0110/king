from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

class ProductContact(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'subject_massage')

class ProductFeedback(admin.ModelAdmin):
    list_display = ('title', 'get_photo', 'name', 'created', 'update', 'is_published')

    list_filter = ('name', 'title', 'created')
    search_fields = ('name', 'title', 'created')
    list_editable = ('is_published',)
    save_on_top = True

    def get_photo(self, obj):
        if obj.file:
            return mark_safe(f'<img src="{obj.file.url}" width=80')
        else:
            return '-'

class ProjectFeedback(admin.ModelAdmin):
    list_display = ('Project_name', 'get_photo', 'kinds', 'created', 'update', 'is_published')

    list_filter = ('Project_name', 'kinds',)
    search_fields = ('Project_name', 'kinds', 'created')
    list_editable = ('is_published',)
    save_on_top = True

    def get_photo(self, obj):
        if obj.file:
            return mark_safe(f'<img src="{obj.file.url}" width=80')
        else:
            return '-'



admin.site.register(Contact, ProductContact)
admin.site.register(Feedback, ProductFeedback)
admin.site.register(Project, ProjectFeedback)