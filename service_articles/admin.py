from django.contrib import admin
from service_articles.models import Cosmetology, CosmetologyAdmin, Gnatology, GnatologyAdmin, Terapy, TerapyAdmin, Ortoped, OrtopedAdmin, Ortodont, OrtodontAdmin, Hygiene, HygieneAdmin, Implant, ImplantAdmin, Parodontology, ParodontologyAdmin

admin.site.register(Cosmetology, CosmetologyAdmin)
admin.site.register(Gnatology, GnatologyAdmin)
admin.site.register(Terapy, TerapyAdmin)
admin.site.register(Ortoped, OrtopedAdmin)
admin.site.register(Ortodont, OrtodontAdmin)
admin.site.register(Hygiene, HygieneAdmin)
admin.site.register(Implant, ImplantAdmin)
admin.site.register(Parodontology, ParodontologyAdmin)

