from django.contrib import admin
from .models import Instrumentation

class InstrumentationAdmin (admin.ModelAdmin):
	list_display = ('name', 'definition', 'imagen')
	search_fields = ('name', 'definition')

# Register your models here.
admin.site.register(Instrumentation, InstrumentationAdmin)