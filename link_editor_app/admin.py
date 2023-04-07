from django.contrib import admin

from link_editor_app.models import (
    Quiz,
    Question,
    Answer,
    Logic
)


# class EmployeeAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'email', 'working_position')
#     search_fields = ('id', 'name', 'email')


# class StoreAdmin(admin.ModelAdmin):
#     list_display = ('id', 'retailer')
#     search_fields = ('id', 'retailer__name')


# class RetailerAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
#     search_fields = ('name',)


# class CityReferenceAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
#     search_fields = ('name',)


# class CityMatchingAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user_city_name')
#     search_fields = ('user_city_name',)


admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Logic)
