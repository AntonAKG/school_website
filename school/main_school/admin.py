from django.contrib import admin

from .models import Teacher, Timetable, Call_schedule, News_main, Gallery, Pride_school

admin.site.register(Teacher)
admin.site.register(Timetable)
admin.site.register(Call_schedule)
admin.site.register(Pride_school)

# admin.site.register(News_main)

class GalleryInline(admin.TabularInline):
    fk_name = 'article'
    model = Gallery


@admin.register(News_main)
class NewsAdmin(admin.ModelAdmin):
    inlines = [GalleryInline, ]
