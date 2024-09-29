

# Register your models here.
# pharmacy/admin.py


# pharmacy/admin.py
from django.contrib import admin

class PetMedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'dosage')

def register_models():
    from .models import PetMedicine  # Import here to avoid circular import
    admin.site.register(PetMedicine, PetMedicineAdmin)
