from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile, Purchases, Avaris


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_role', 'get_birth_date', 'get_agency',)
    list_select_related = ('profile',)

    def get_agency(self, instance):
        return instance.profile.agency

    get_agency.short_description = 'User`s Agency'

    def get_role(self, instance):
        return instance.profile.role

    get_role.short_description = 'User Role'

    def get_birth_date(self, instance):
        return instance.profile.birthDate

    get_birth_date.short_description = 'Birth Date'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(Purchases)
admin.site.register(Avaris)