from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile


class CustomUserAdmin(UserAdmin):
    model = User

    list_display = ("email", "is_superuser", "is_active",)
    list_filter = ("email", "is_superuser", "is_active",)
    serching_fields = ('email',)
    ordering = ('email',)

    # vaghti vard info yek user beshim field hayi ke dar fieldset moshakhas kardim namayesh dade mishe
    fieldsets = (
        ('Authentication', {
            "fields": (
                'email', 'password'
            ),
        }),
        ('Permissions', {
            "fields": (
                'is_staff', 'is_active', 'is_superuser'
            ),
        }),
        ('Group permission', {
            "fields": (
                'groups', 'user_permissions'
            ),
        }),
        ('Important dates', {
            "fields": (
                'last_login',
            ),
        }),
    )

    # vaghti bekhaim user besazim baiad dar add_fieldsets begim ke karbar baiad che field haei ro poor kone baraye sakht user
    # password1 va password2 dar models man tarif nashode vali default dar django tarif shode ke baiad moghe sakhte user az password1 va password2 estefade konim
    # age faghat az field password estefade konim user sakhte nemishe
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser')}
        ),
    )
    


admin.site.register(Profile)
admin.site.register(User, CustomUserAdmin)