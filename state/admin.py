from django.contrib import admin
from .models import State, Statistic
from django_admin_inline_paginator.admin import TabularInlinePaginated

# Register your models here.

class Statistic(TabularInlinePaginated):
    per_page = 60
    model = Statistic

@admin.register(State)
class Post(admin.ModelAdmin):
    inlines = [Statistic]
    class Meta:
        model = State