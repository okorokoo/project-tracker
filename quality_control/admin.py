from django.contrib import admin
from .models import BugReport, FeatureRequest


class BugReportInline(admin.TabularInline):
    model = BugReport
    extra = 0
    fields = ('title', 'description', 'status', 'priority', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    can_delete = True
    show_change_link = True


class FeatureRequestInline(admin.TabularInline):
    model = FeatureRequest
    extra = 0
    fields = ('title', 'description', 'status', 'priority', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    can_delete = True
    show_change_link = True


@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'created_at', 'status', 'priority')
    list_filter = ('status', 'priority', 'project', 'task')
    search_fields = ('name', 'description')

    # inlines = [TaskInline]


@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'task', 'project', 'created_at', 'status', 'priority')
    list_filter = ('status', 'priority', 'project', 'task')
    search_fields = ('name', 'description')