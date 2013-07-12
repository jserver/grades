from django.contrib import admin

from .models import Action, Cuisine, Violation, WebExtract

class ActionAdmin(admin.ModelAdmin):
    pass

class CuisineAdmin(admin.ModelAdmin):
    pass

class ViolationAdmin(admin.ModelAdmin):
    pass

class WebExtractAdmin(admin.ModelAdmin):
    pass

admin.site.register(Action, ActionAdmin)
admin.site.register(Cuisine, CuisineAdmin)
admin.site.register(Violation, ViolationAdmin)
admin.site.register(WebExtract, WebExtractAdmin)

