# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Award, Member

class AwardAdmin(admin.ModelAdmin):
    fields = ['rank', 'competition', 'institution', 'participant', 'year']
    list_display = ['rank', 'competition', 'institution', 'participant', 'year']

class MemberAdmin(admin.ModelAdmin):
    fields = ['role', 'division', 'name', 'email', 'linkedin', 'photo']
    list_display = ['role', 'division', 'name', 'email', 'linkedin', 'photo']

admin.site.register(Award, AwardAdmin)
admin.site.register(Member, MemberAdmin)