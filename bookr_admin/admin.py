from django.contrib import admin

# Register your models here.


class BookrAdmin(admin.AdminSite):
    site_header = "Administracja witryną Bookr"
    site_title = "Moja aplikacja internetowa Django"
    index_title = "Panel administracyjny"
