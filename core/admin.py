from django.contrib import admin
from .models import ValentineVideo
# Register your models here.

@admin.register(ValentineVideo)
class ValentineVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'uploaded_at')
    list_filter = ('is_active', 'uploaded_at')