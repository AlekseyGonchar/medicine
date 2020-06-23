from django.contrib import admin

from .models import Medicine, DoseVariant


class DoseVariantInline(admin.TabularInline):
    model = DoseVariant


class MedicineAdmin(admin.ModelAdmin):
    exclude = ['local']
    inlines = [
        DoseVariantInline,
    ]


admin.site.register(Medicine, MedicineAdmin)
