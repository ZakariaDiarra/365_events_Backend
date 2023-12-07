from django.contrib import admin
from .models import Event, Category, UserProfile, Reservation
from django.contrib.auth.models import User

class EventAdmin(admin.ModelAdmin):
    list_display = ('title','description', 'date', 'location', 'imageUrl')
    search_fields = ['title', 'description', 'date', 'location', 'imageUrl']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'imageUrl')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'bio', 'birthday', 'photo')

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'tickets')
    search_fields = ['user__username', 'event__title', 'tickets']




admin.site.register(Event, EventAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Reservation, ReservationAdmin)