from django.contrib import admin
from .models import MedicalUser, Appointment, Entity

admin.site.register(MedicalUser)
admin.site.register(Appointment)
admin.site.register(Entity)

# from django.contrib import admin
# from django.contrib.admin import TabularInline

# class MultiDBModelAdmin(admin.ModelAdmin):
#     # A handy constant for the name of the alternate database.

#     def save_model(self, request, obj, form, change):
#         # Tell Django to save objects to the specified database.
#         obj.save()

#     def delete_model(self, request, obj):
#         # Tell Django to delete objects from the specified database.
#         obj.delete()

#     def get_queryset(self, request):
#         # Tell Django to look for objects on the specified database.
#         return super().get_queryset(request)

#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         # Tell Django to populate ForeignKey widgets using a query
#         # on the specified database.
#         return super().formfield_for_foreignkey(
#             db_field, request, **kwargs
#         )

#     def formfield_for_manytomany(self, db_field, request, **kwargs):
#         # Tell Django to populate ManyToMany widgets using a query
#         # on the specified database.
#         return super().formfield_for_manytomany(
#             db_field, request, **kwargs
#         )

# class MultiDBTabularInline(TabularInline):
#     using = "db_1"  # Adjust this according to your database configuration

#     def get_queryset(self, request):
#         # Tell Django to look for inline objects on the specified database.
#         return super().get_queryset(request)

#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         # Tell Django to populate ForeignKey widgets using a query
#         # on the specified database.
#         return super().formfield_for_foreignkey(
#             db_field, request, **kwargs
#         )

#     def formfield_for_manytomany(self, db_field, request, **kwargs):
#         # Tell Django to populate ManyToMany widgets using a query
#         # on the specified database.
#         return super().formfield_for_manytomany(
#             db_field, request, **kwargs
#         )


# # Create a custom AdminSite for db_1
# db_1_admin_site = admin.AdminSite(name='db_1_admin')
# db_1_admin_site.register(Entity, MultiDBModelAdmin)
# db_1_admin_site.register(Appointment, MultiDBModelAdmin)

# # Create a custom AdminSite for db_2
# db_2_admin_site = admin.AdminSite(name='db_2_admin')
# db_2_admin_site.register(MedicalUser, MultiDBModelAdmin)