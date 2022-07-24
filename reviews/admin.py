from django.contrib import admin
from reviews.models import Publisher, Contributor, Book, BookContributor, Review


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "isbn")
    list_filter = ("publisher",)
    date_hierarchy = "publication_date"
    search_fields = ("title", "publisher__name")

    def get_publisher(self, obj):
        return obj.publisher.name


class ReviewAdmin(admin.ModelAdmin):
    exclude = ("date_edited",)
    fieldsets = ((None, {"fields": ("creator", "book")}),
                 ("Treść recenzji", {"fields": ("content", "rating")}))


class ContributorAdmin(admin.ModelAdmin):
    list_display = ("last_names", "first_names")
    search_fields = ("last_names__startswith", "first_names")
    list_filter = ("last_names",)

# Register your models here.


admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review, ReviewAdmin)
