from feitec.projeto.models import *
from django.contrib import admin

class IntegranteInline(admin.TabularInline):
    model = Integrante
    extra = 2
class ProjAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['nomeProj']}),
		(None, {'fields': ['resumoProj']}),
        (None, {'fields': ['materialProj']}),
        (None, {'fields': ['campusProj']}),
		(None, {'fields': ['salaProj']}),
        (None, {'fields': ['equipamentoProj']}),
        (None, {'fields': ['area']}),
        (None, {'fields': ['situacao']}),
    ] 
    inlines= [IntegranteInline]
    list_display=('nomeProj','deletar')

    def deletar(self,object):
        return '<a href=/admin/projeto/%s/delete/>Deletar<a/>' %(object.id)
    deletar.allow_tags = True

admin.site.register(Area)
admin.site.register(Campus)
admin.site.register(CertificadoIntegrante)
admin.site.register(CertificadoProfessor)
admin.site.register(Integrante)
admin.site.register(Projeto)
admin.site.register(Professor)


