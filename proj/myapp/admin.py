from django.contrib import admin

from myapp.models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display=['id','name','address']
    list_editable=('name','address')
    list_filter=('name','address')
    search_fields=('name','address')

# Register your models here.
admin.site.register(Person,PersonAdmin)