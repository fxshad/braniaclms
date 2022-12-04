from django.contrib import admin
from mainapp.models import News, Course, Lesson, CourseTeacher
from django.utils.html import format_html

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(CourseTeacher)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'deleted')
    list_filter = ('deleted', 'created_at')
    search_fields = ('title', 'intro', 'body',)
    ordering = ('pk',)
    list_per_page = 3
    actions = ('mark_as_deleted',)

    def slug(self, obj):
        return format_html(
            '<a href="{}" target="_blank">{}</a>',
            obj.title.lower().replace(' ', '_'),
            obj.title
        )
    slug.short_description = 'Слаг'

    def mark_as_deleted(selfs, request, queryset):
        queryset.update(deleted=True)

    mark_as_deleted.short_description = "пометить удаленным"
