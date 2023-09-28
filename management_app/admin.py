from django.contrib import admin

from .models import Customer, Contact, Contractor

class ContactInline(admin.StackedInline):  # or admin.TabularInline for a compact style
    model = Contact
    extra = 1  # Number of extra empty forms to display

class CustomerAdmin(admin.ModelAdmin):
    inlines = [ContactInline,]

class CustomerInline(admin.StackedInline):  # or admin.TabularInline for a compact style
    model = Customer
    extra = 0  # Number of extra empty forms to display
    fields = ('company_name',)
    readonly_fields = ('company_name',)

class ContractorAdmin(admin.ModelAdmin):
    inlines = [CustomerInline,]

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Contact)
admin.site.register(Contractor, ContractorAdmin)