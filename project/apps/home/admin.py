from django.contrib import admin
from .models import DocumentModel, ImageModel, CalendarModel, AboutUsModel, GoalModel
from parler.admin import TranslatableAdmin


class ModelAdmin(TranslatableAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(DocumentModel, ModelAdmin)
admin.site.register(CalendarModel, ModelAdmin)
admin.site.register(ImageModel)


@admin.register(AboutUsModel)
class AboutUsAdmin(TranslatableAdmin):
    list_display = ('id', 'selected')
    list_display_links = ('id',)
    search_fields = ('description',)


@admin.register(GoalModel)
class GoalAdmin(TranslatableAdmin):
    list_display = ('id', 'goal', 'disabled')
    list_display_links = ('id',)
    search_fields = ('goal',)
