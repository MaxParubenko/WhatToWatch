from django.contrib import admin
from .models import WatchList, Movie, Review, Genre, Director, Actor
from django.utils.safestring import mark_safe
from django import forms 
from ckeditor_uploader.widgets import CKEditorUploadingWidget




class MovieAdminForm(forms.ModelForm):
    # poster = forms.CharField(label='Постер',widget=CKEditorUploadingWidget())
    description = forms.CharField(label='Опис',widget=CKEditorUploadingWidget())


    class Meta:
        model = Movie
        fields = '__all__'


class ReviewInLine(admin.TabularInline):
    model = Review
    extra = 1
    readonly_fields = ('user',)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'release_date', 'url')
    list_filter = ('year',)
    list_display_links = ("title",)
    search_fields = ('title', 'genre__name', 'year')
    inlines = [ReviewInLine]
    save_on_top = True
    save_as = True
    form = MovieAdminForm
    readonly_fields = ('get_image',)
    fieldsets = (
        (None, {
            'fields': (('title', 'get_image'),)
        }),
        (None, {
            'fields': (('trailer',),)
        }),
        (None, {
            'fields': (('description', 'poster', 'url'),)
        }),
        (None, {
            'fields': (('year', 'release_date'),)
        }),
        (None, {
            'fields': (('director', 'actors', 'genre'),)
        }),


    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" height="110"')

    get_image.short_description = "Постер"


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', "url")
    list_filter = ('name',)
    list_display_links = ("name",)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', "movie", 'parent', 'id')
    readonly_fields = ('user',)


@admin.register(WatchList)
class WatchListAdmin(admin.ModelAdmin):
    list_display = ('user',)
    readonly_fields = ('user',)


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="50" height="60"')

    get_image.short_description = "Зображення"


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ("name", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="50" height="60"')

    get_image.short_description = "Зображення"
