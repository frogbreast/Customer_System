from django.contrib import admin

# Register your models here.
from app.models import UserOverview, UsageRecord

@admin.register(UserOverview)
class UserOverviewAdmin(admin.ModelAdmin):
    pass

@admin.register(UsageRecord)
class UsageRecordAdmin(admin.ModelAdmin):
    pass
