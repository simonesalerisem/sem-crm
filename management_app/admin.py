from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Customer, Contact, Contractor, Order, Job

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

class JobInline(admin.TabularInline):
    model = Job
    extra = 1  # number of extra forms to display

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'customer', 'total_hours', 'download_button']
    inlines = [JobInline]

    def download_button(self, obj):
        return format_html('<a class="button" href="{}">Download Order</a>', 
                           reverse('pdf_view', args=[obj.id]))
    download_button.short_description = 'Download Order'
    download_button.allow_tags = True

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Contractor, ContractorAdmin)



