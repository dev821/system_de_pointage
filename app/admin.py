from django.contrib import admin

from .models import Employe, Pointage
# Register your models here.

class EmployeAdmin(admin.ModelAdmin):
    list_display = ('lastName', 'firstName', 'address', 'tel')
    list_filter = ('lastName', 'firstName')

class PointageAdmin(admin.ModelAdmin):
    list_display = ('idEmploye', 'dateEmprunt', 'status')
    list_filter = ('idEmploye', 'dateEmprunt', 'status')



admin.site.register(Employe, EmployeAdmin)
admin.site.register(Pointage, PointageAdmin)