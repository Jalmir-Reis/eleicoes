from django.contrib import admin
from .models import News, Timer, Typed, Music, Default, Images, Home

# NEWSLETTERS
class NewsAdmin(admin.ModelAdmin):
    readonly_fields = ['email']
    list_display = ['email']
    search_fields: ['email']
    list_per_page: 10
admin.site.register(News, NewsAdmin)

# TIMER
class TimerAdmin(admin.ModelAdmin):
    list_display = ['timer']
    # Função para ID (timer) unico
    def has_add_permission(self, *args, **kwargs):
        return not Timer.objects.exists()
admin.site.register(Timer, TimerAdmin)

# TYPED
class TypedAdmin(admin.ModelAdmin):
    list_display = ['fixo']
    def has_add_permission(self, *args, **kwargs):
        return not Typed.objects.exists()
admin.site.register(Typed, TypedAdmin)

# MUSIC
class MusicAdmin(admin.ModelAdmin):
    list_display = ['title_music']
    def has_add_permission(self, *args, **kwargs):
        return not Music.objects.exists()
admin.site.register(Music, MusicAdmin)

# DEFAULT
class DefaultAdmin(admin.ModelAdmin):
    list_display = ['titulo']
    def has_add_permission(self, *args, **kwargs):
        return not Default.objects.exists()
admin.site.register(Default, DefaultAdmin)

# IMAGES
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['titulo']
    def has_add_permission(self, *args, **kwargs):
        return not Music.objects.exists()
admin.site.register(Images, ImagesAdmin)

# HOME
class HomeAdmin(admin.ModelAdmin):
    list_display = ['home_title']
    def has_add_permission(self, *args, **kwargs):
        return not Home.objects.exists()
admin.site.register(Home, HomeAdmin)
