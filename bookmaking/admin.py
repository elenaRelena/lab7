from django.contrib import admin
from .models import User1 



class MyAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'stake', 'contacts', 'bank_account')
    list_filter = ('stake',)
    search_fields = ['name']
    
admin.site.register(User1, MyAdmin)