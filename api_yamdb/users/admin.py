from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class CategoriesAdmin(admin.ModelAdmin):
    """ Categories admin"
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'role'
    )
    search_fields = ('username',)
    list_filter = ('username',)
    empty_value_display = '-пусто-'
