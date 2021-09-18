from django.contrib import admin
from .models import Upload


class UploadAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'file']


admin.site.register(Upload, UploadAdmin)
