from django.contrib import admin
from .models import Test

class admin_Test(admin.ModelAdmin):
	list_display = [
        'id',
		'comments',
    ]
admin.site.register(Test, admin_Test)
