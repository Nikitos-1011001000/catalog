from django.contrib import admin
from django.contrib.auth import get_user_model


User = get_user_model()


class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
    )

    list_filter = (
        'is_active',
        'is_staff',
        'groups',
    )

    search_fields = (
        'email',
        'first_name',
        'last_name',
    )

    ordering = ('email',)

    filter_horizontal = (
        'groups',
        'user_permissions',
    )


try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass


admin.site.register(User, CustomUserAdmin)

# Register your models here.
