from django.contrib import admin
from .models import Account
# Register your models here.

class AccountAdmin(admin.ModelAdmin):
  list_display = ('email','username','phone','is_active','last_active','registered_on')
  readonly_fields = ('last_active','registered_on')
  list_display_links = ('email','username','phone','is_active')
  odering = ('-last_active')

admin.site.register(Account, AccountAdmin)
