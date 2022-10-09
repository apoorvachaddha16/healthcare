from django.contrib import admin
from .models import patient
# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    list_display = ['name','wardno', 'saline']




admin.site.register(patient, MessageAdmin)

