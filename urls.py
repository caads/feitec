from django.conf.urls.defaults import *
from django.conf import settings

from feitec.projeto.views import *
from django.contrib import admin

from django.views.generic.simple import direct_to_template
from django.views.generic.date_based import archive_index

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'feitec.views.home', name='home'),
    # url(r'^feitec/', include('feitec.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^cadastrar/', 'feitec.projeto.views.cadastrar'),
    (r'^$', 'feitec.projeto.views.principal'),
    (r'^filtrar_area_gerencia/(?P<codigo>\d+)/$', 'feitec.projeto.views.filtrar_area_gerencia'),
    (r'^mostra_dados_projeto/(?P<codigo>\d+)/$', 'feitec.projeto.views.mostra_dados_projeto'),
    (r'^criar_projeto/(?P<numero>\d+)/(?P<numero2>\d+)/$','feitec.projeto.views.criar_projeto'),
	(r'^cadastrar_projeto/$', 'feitec.projeto.views.cadastrar_projeto'),	    
    (r'^projeto/(?P<projeto_codProj>\d+)/$', 'feitec.projeto.views.projeto'),
    (r'^editar_gerencia/(?P<codigo>\d+)/$', 'feitec.projeto.views.editar_gerencia'),
    (r'^editar_gerencia2/(?P<codigo>\d+)/$', 'feitec.projeto.views.editar_gerencia2'),
    (r'^apagar_projeto/(?P<codigo>\d+)/$', 'feitec.projeto.views.apagar_projeto'),
    (r'^todos_participantes/$','feitec.projeto.views.todos_participantes'),
    (r'^todos_professores/$','feitec.projeto.views.todos_professores'),    
    (r'^busca_participante/$','feitec.projeto.views.busca_participante'),
    (r'^busca_professor/$','feitec.projeto.views.busca_professor'),
    (r'^principal_certificado/$','feitec.projeto.views.principal_certificado'),
    (r'^editar_integrante/(?P<codigo>\d+)/$','feitec.projeto.views.editar_integrante'), 
    (r'^emitir/(?P<codigo>\d+)/$','feitec.projeto.views.emitir'),
    (r'^emitir_prof/(?P<codigo>\d+)/$','feitec.projeto.views.emitir_prof'),
    (r'^certificado/(?P<codigo>\d+)/(?P<codCert>\d+)/$','feitec.projeto.views.certificado'),
    (r'^certificado_prof/(?P<codigo>\d+)/(?P<codCert>\d+)/$','feitec.projeto.views.certificado_prof'),
    (r'^numerar_participantes/(?P<codigo>\d+)/$','feitec.projeto.views.numerar_participantes'),
    (r'^criar_alterar/(?P<codigo>\d+)/$','feitec.projeto.views.criar_alterar'),
    (r'^login/', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    (r'^consultar/$','feitec.projeto.views.consultar_esqueci'),
    (r'^resultado_esqueci/$','feitec.projeto.views.resultado_esqueci'),
    (r'^mudar_senha/$', 'django.contrib.auth.views.password_change',{'template_name': 'mudar_senha.html'}, 'mudar_senha'),
    (r'^mudar_senha/concluido/$', 'django.contrib.auth.views.password_change_done',{'template_name': 'mudar_senha_concluido.html'}, 'mudar_senha_concluido'),
    (r'^logout/', 'django.contrib.auth.views.logout', {'template_name': 'logout.html', 'next_page': '/login'}),
    (r'^media/(.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
)
    
