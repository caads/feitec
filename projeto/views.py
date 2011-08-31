#encoding: utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from feitec.projeto.models import *
from django.forms import ModelForm, TextInput, PasswordInput, HiddenInput
from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from forms import CadastroForm
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory
from django.contrib.localflavor.br.forms import BRCPFField, BRPhoneNumberField
from django.core.mail import send_mail, get_connection, EmailMessage
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from django.conf import settings
from cStringIO import StringIO
from datetime import datetime
import datetime
import os

#Pagina principal
@login_required
def principal(request):
    if request.method == "POST":
        numero = request.POST['professor']
        numero2 = request.POST['integrante']
        return HttpResponseRedirect(reverse('feitec.projeto.views.criar_projeto' ,args=[numero,numero2]))
    else:
        usuario = request.user
        nome = request.user.username
        gerente ='gerencia'   
        if (nome==gerente):
            #projeto = Projeto.objects.all()
            cont = Projeto.objects.filter(situacao="Aprovado").count()
            #return render_to_response('principal.html',{'projeto':projeto,'usuario':usuario,'nome':nome, 'cont':cont},context_instance=RequestContext(request)) 
            area = Area.objects.all()
            return render_to_response('principal.html',{'area':area,'usuario':usuario,'nome':nome,'cont':cont,},context_instance=RequestContext(request))
            
        else:
            projeto = Projeto.objects.filter(criador = usuario)
            return render_to_response('principal.html',{'projeto':projeto,'usuario':usuario,},context_instance=RequestContext(request))

#Cadastro de Usuario
def cadastrar(request):
    if request.POST:
        form = CadastroForm(request.POST)
        if form.is_valid():
            novo_usuario = form.save()
            return HttpResponseRedirect('/')
        else:
            return render_to_response('cadastrar.html', {'form': form}, context_instance=RequestContext(request))
    else:
        form = CadastroForm()
        return render_to_response('cadastrar.html', {'form': form}, context_instance=RequestContext(request))

def consultar_esqueci(request):
    if request.method == "POST":
        return render_to_response('404.html')
    else:
        return render_to_response('esqueci_email.html', context_instance = RequestContext(request))

def resultado_esqueci(request):
    if request.method == 'POST':
        try:
            email = request.POST['email']
            consulta = User.objects.get(email=email) 
            mensagem  = 'Foi enviado ao seu email sua nova senha:' 
            random = User.objects.make_random_password(length=10, allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789')
            consulta.set_password(random)
            subject = 'Feitec Nova Senha:'
            message = ('Sua nova senha é:' + random)   
            from_email = ''#email remetente
            connection = get_connection(username = '', password ='')#email e senha conexão
            send_email = EmailMessage(subject, message , from_email, [consulta.email], connection = connection)
            send_email.content_subtype = "html"
            send_email.send()
            consulta.save()  
        except ObjectDoesNotExist:
            consulta = ''
            mensagem = 'Este email não está cadastrado em nosso sistema!'
        return render_to_response('esqueci_email.html',{ 'mensagem' : mensagem,}, context_instance = RequestContext(request))
    else:
        return render_to_response('404.html')


#Cadastro de Projeto get	
@login_required
def criar_projeto(request, numero , numero2):
    usuario = request.user
    if request.method == "POST":
        return render_to_response('404.html')
    else:
        teste = int(numero)
        teste2 = int(numero2)
        IntegranteFormSet = inlineformset_factory(Projeto, Integrante, form=ProjetoModelForm , extra=teste)
        ProfessorFormSet = inlineformset_factory(Projeto, Professor, form=ProjetoModelForm , extra=teste2)
        inscricao = {
            'criador':usuario,
            'area':1,
            'campus':1,
        }
        form = ProjetoModelForm(inscricao)
        formset = IntegranteFormSet()
        formset2 = ProfessorFormSet()
        return render_to_response('cadastrar_projeto.html', {'formset':formset,'formset2':formset2,'form': form,'usuario':usuario,'teste':teste,'teste2':teste2}, context_instance=RequestContext(request))

#Cadastro de Projeto post	
@login_required
def cadastrar_projeto(request):
    IntegranteFormSet = inlineformset_factory(Projeto, Integrante, form=ProjetoModelForm)
    ProfessorFormSet = inlineformset_factory(Projeto, Professor, form=ProjetoModelForm)
    if request.method == 'POST':
        form = ProjetoModelForm(request.POST)
        if form.is_valid():
            projeto = form.save(commit=False)
            formset = IntegranteFormSet(request.POST, instance=projeto)
            formset2 = ProfessorFormSet(request.POST, instance=projeto)
            if formset.is_valid():
                c = form.save()
                d = formset.save()
                e = formset2.save()
                return HttpResponseRedirect('/')
            else:
                return render_to_response(form.errors)
        else:
            return render_to_response('projeto_existe.html',context_instance=RequestContext(request))
    else:
        return render_to_response('404.html')

#Editar projeto
@login_required
def mostra_dados_projeto(request, codigo):
    usuario = request.user
    projeto = get_object_or_404(Projeto, pk=codigo)
    IntegranteFormSet = inlineformset_factory(Projeto, Integrante,extra = 2)
    ProfessorFormSet = inlineformset_factory(Projeto, Professor,extra = 2)
    codigo = projeto.codProj
    if request.method == 'POST':
        f = ProjetoModelForm(request.POST, instance=projeto)
        if f.is_valid():
            project = f.save(commit=False)
            formset = IntegranteFormSet(request.POST, instance=project)
            formset2 = ProfessorFormSet(request.POST, instance=project)
            if formset.is_valid():
                c = f.save()
                d = formset.save()
                e = formset2.save()
                return HttpResponseRedirect('/')
            else:
                return render_to_response(form.errors)
        else:
            return render_to_response(form.errors)
    else:	
        f = ProjetoModelForm(instance=projeto)
        formset = IntegranteFormSet(instance=projeto)
        formset2 = ProfessorFormSet(instance=projeto)
        return render_to_response('alterar_dados.html', {'formset':formset,'formset2':formset2,'form':f, 'codigo':codigo,'usuario':usuario,},context_instance=RequestContext(request))

@login_required
def criar_alterar(request,codigo):
    usuario = request.user
    if request.method == "POST":
        projeto = get_object_or_404(Projeto, pk=codigo)
        IntegranteFormSet = inlineformset_factory(Projeto, Integrante,extra = 2)
        ProfessorFormSet = inlineformset_factory(Projeto, Professor,extra = 2)
        codigo = projeto.codProj
        integrante = request.POST['integrante']
        professor = request.POST['professor']
        teste = int(integrante)
        teste2 = int(professor)
        IntegranteFormSet = inlineformset_factory(Projeto, Integrante,extra = teste)
        ProfessorFormSet = inlineformset_factory(Projeto, Professor,extra = teste2)
        f = ProjetoModelForm(instance=projeto)
        formset = IntegranteFormSet(instance=projeto)
        formset2 = ProfessorFormSet(instance=projeto)
        return render_to_response('alterar_dados.html', {'formset':formset,'formset2':formset2,'form':f, 'codigo':codigo,'usuario':usuario},context_instance=RequestContext(request))
    else:
        return render_to_response('404.html')

@login_required
def numerar_participantes(request,codigo):
    usuario = request.user
    if request.method == "GET":
        projeto = Projeto.objects.get(codProj = codigo)
        integrante = Integrante.objects.filter(projeto = codigo)
        professor = Professor.objects.filter(projeto = codigo)	
        return render_to_response('numerar_participantes.html',{'codigo':codigo,'projeto':projeto,'integrante':integrante,'professor':professor,'usuario':usuario},context_instance=RequestContext(request))
    else:
        return render_to_response('404.html')

#Apagar projeto
@login_required
def apagar_projeto(request, codigo):
    projeto = get_object_or_404(Projeto, pk=codigo)
    projeto.delete()
    return HttpResponseRedirect('/')

#Projeto sem poder editar
@login_required
def projeto(request, projeto_codProj):
    usuario = request.user
    if request.method == "POST":
        return render_to_response('404.html')
    else:
        projeto = Projeto.objects.get(codProj = projeto_codProj)
        integrante = Integrante.objects.filter(projeto = projeto_codProj)
        professor = Professor.objects.filter(projeto = projeto_codProj)	
        usuario = request.user
        return render_to_response('projeto.html',locals(),context_instance=RequestContext(request))

#Editar situacao de Integrante
@login_required
def editar_integrante(request, codigo):
    usuario = request.user
    inte = get_object_or_404(Integrante, pk=codigo)
    if request.method == 'POST':
        form = SituacaoIntModelForm(request.POST, instance=inte)
        if form.is_valid():
            c = form.save()
            return HttpResponseRedirect('/')
        else:
            return render_to_response(form.errors)
    else:
        form = SituacaoIntModelForm(instance=inte)
        integrante = Integrante.objects.get(codIntegrante = codigo)
        return render_to_response('editar_integrante.html',{'form':form, 'integrante':integrante, 'codigo':codigo,'usuario':usuario,}, context_instance=RequestContext(request))
     	
#Editar Sala e avaliar projeto
@login_required
def editar_gerencia(request, codigo):
    usuario = request.user
    projeto = get_object_or_404(Projeto, pk=codigo)
    codigo = projeto.codProj
    if request.method == 'POST':
        form = ProjetoGerenciaForm(request.POST, instance=projeto)
        if form.is_valid():
            c = form.save()
            return HttpResponseRedirect('/')
        else:
            return render_to_response(form.errors)
    else:	
        form = ProjetoGerenciaForm(instance=projeto)
        professor = Professor.objects.filter(projeto = codigo)        
        integrante = Integrante.objects.filter(projeto = codigo)
        projeto = Projeto.objects.get(codProj = codigo)
        return render_to_response('editar_gerencia.html', {'form':form, 'codigo':codigo,'integrante':integrante,'projeto':projeto, 'professor':professor,'usuario':usuario},context_instance=RequestContext(request))
		

#Editar Sala apos avaliacao do projeto
@login_required
def editar_gerencia2(request, codigo):
    usuario = request.user
    projeto = get_object_or_404(Projeto, pk=codigo)
    codigo = projeto.codProj
    if request.method == 'POST':
        form = ProjetoGerenciaModelForm(request.POST, instance=projeto)
        if form.is_valid():
            c = form.save()
            return HttpResponseRedirect('/')
        else:
            return render_to_response(form.errors)
    else:	
        form = ProjetoGerenciaModelForm(instance=projeto)
        integrante = Integrante.objects.filter(projeto = codigo)
        professor = Professor.objects.filter(projeto = codigo)
        projeto = Projeto.objects.get(codProj = codigo)
        return render_to_response('editar_gerencia2.html', {'form':form, 'codigo':codigo,'integrante':integrante,'projeto':projeto,'professor':professor,'usuario':usuario,},context_instance=RequestContext(request))

#Exibir todos participantes
@login_required
def todos_participantes(request):
     usuario = request.user
     part = Integrante.objects.all()
     return render_to_response('todos_participantes.html',locals(), context_instance=RequestContext(request))

#Exibir todos professores
@login_required
def todos_professores(request):
     usuario = request.user
     prof = Professor.objects.all()
     return render_to_response('todos_professores.html',locals(), context_instance=RequestContext(request))

#Pagina principal dos certificados
@login_required
def principal_certificado(request):
     usuario = request.user
     return render_to_response('certificado.html',locals(), context_instance = RequestContext(request))

#Busca de participante
@login_required
def busca_participante(request):
    usuario = request.user
    if request.method =='POST':
        nome = request.POST['nome']
        part = Integrante.objects.filter(nomeIntegrante__icontains=nome)
        return render_to_response('buscapart.html',{'part':part,'usuario':usuario,}, context_instance=RequestContext(request))
    else:
        return render_to_response('buscapart.html',{'usuario':usuario}, context_instance=RequestContext(request))

#Busca de professor
@login_required
def busca_professor(request):
    usuario = request.user
    if request.method =='POST':
        nome = request.POST['nome']
        prof = Professor.objects.filter(nomeProfessor__icontains=nome)
        return render_to_response('busca_prof.html',{'prof':prof}, context_instance=RequestContext(request))
    else:
        return render_to_response('busca_prof.html', context_instance=RequestContext(request)) 

@login_required
def filtrar_area_gerencia(request,codigo):
    usuario = request.user
    if request.method == "GET":
        projeto = Projeto.objects.filter(area = codigo)
        cont = Projeto.objects.filter(situacao="Aprovado", area=codigo).count()
        return render_to_response('gerencia_area.html',{'projeto':projeto,'cont':cont,'usuario':usuario},context_instance=RequestContext(request))
    else:
        return render_to_response('404.html')

#emitir o certificado do professor
@login_required
def emitir_prof(request, codigo):
    usuario = request.user
    x = get_object_or_404(Professor, pk=codigo)
    try:
        certificado_prof = CertificadoProfessor.objects.get(professor = codigo)
    except ObjectDoesNotExist:
        certificado_prof = CertificadoProfessor.objects.create(professor = x) 
    if request.method =='POST':    
        f= DadosCertModelFormProfessor(request.POST,instance = certificado_prof)
        if f.is_valid():        
            c = f.save()
            return HttpResponseRedirect(reverse('feitec.projeto.views.certificado_prof', args=[x.codProfessor, c.codCert]))
        else:
            render_to_response(f.errors)
    else:
        f= DadosCertModelFormProfessor(instance = certificado_prof)
        return render_to_response('dados_certificado_prof.html', {'c':x, 'f':f,'usuario':usuario}, context_instance=RequestContext(request))

#gerar pdf certificado do professor
@login_required
def certificado_prof(request,codigo, codCert): 
        response = HttpResponse (mimetype='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=certificado.pdf'
        buffer = StringIO()
        p = canvas.Canvas(buffer)
        
        d = get_object_or_404(CertificadoProfessor, pk=codCert)
        c = get_object_or_404(Professor, pk=codigo)
        e = get_object_or_404(Projeto, nomeProj=c.projeto)
        projeto = str (e.nomeProj)
        area = str (e.area)
        dia = str (d.data)
        mes = str (d.mes)
        ano = str (d.ano)
        p.translate(inch,inch)
        p.setFont("Helvetica", 14)
        p.rotate(90)
        artur = os.path.join(settings.PROJECT_ROOT_PATH,"carlos.png") 
        jeff = os.path.join(settings.PROJECT_ROOT_PATH,"jeff.png") 
        p.drawImage(artur, 1*inch,-400, width=91,height=50)
        p.drawImage(jeff, 7*inch,-400, width=180,height=50)
        p.setFont("Helvetica-BoldOblique", 12)
        p.drawString(1*inch, -220, "Certificamos que " + c.nomeProfessor + " coordenou o projeto " + projeto + ", área temática " + area + " ")  
        p.drawString(0.5*inch, -240, "apresentado na FEITEC 2011 – Feira de Ciência Tecnologia e Inovação do IFF – Campus Campos Centro,")
        p.drawString(0.5*inch, -260, " realizada na 19ª Semana do Saber Fazer Saber, nos dias 7,8 e 9 de setembro de 2011.")
        p.drawString(6*inch, -290, "Campos dos Goytacazes, " + dia + " de " + mes + " de " + ano)      
        p.drawString(0.5*inch, -415, "Carlos Artur de Carvalho Arêas")  
        p.setFont("Helvetica-Oblique", 12)
        p.drawString(0.5*inch, -430, "Diretor do Departamento de Desenvolvimento") 
        p.drawString(0.5*inch, -445, "Institucional e Extensão Campus Campos-Centro")
        p.setFont("Helvetica-BoldOblique", 12)
        p.drawString(7*inch, -415, "Jefferson Manhães de Azevedo")
        p.setFont("Helvetica-Oblique", 12)  
        p.drawString(7*inch, -430, "Diretor Geral do IFF") 
        p.drawString(7*inch, -445, "Campus Campos-Centro")
        p.setFont("Helvetica-Oblique", 8)
        p.drawString(8*inch,-500, "O presente certificado foi registrado sob o n." + d.numeroCert)        
        p.drawString(8*inch, -510, "No Livro n. " + d.livroCert + " em " + d.dataCert)
        p.showPage()
        p.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

#emitir certificado do participante
@login_required
def emitir(request, codigo):
    usuario = request.user
    x = get_object_or_404(Integrante, pk=codigo)
    try:
        certificado = CertificadoIntegrante.objects.get(integrante = codigo)
    except ObjectDoesNotExist:
        certificado = CertificadoIntegrante.objects.create(integrante = x)
    if request.method =='POST':    
        f= DadosCertModelFormIntegrante(request.POST,instance = certificado)
        if f.is_valid():        
            c = f.save()
            return HttpResponseRedirect(reverse('feitec.projeto.views.certificado', args=[x.codIntegrante, c.codCert]))
        else:
            render_to_response(f.errors)
    else:
        f= DadosCertModelFormIntegrante(instance = certificado)
        return render_to_response('dadoscertificado.html', {'c':x, 'f':f,'usuario':usuario,}, context_instance=RequestContext(request))

#gerar pdf do certificado do participante
@login_required
def certificado(request,codigo, codCert): 
        response = HttpResponse (mimetype='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=certificado.pdf'
        buffer = StringIO()
        p = canvas.Canvas(buffer)
        
        d = get_object_or_404(CertificadoIntegrante, pk=codCert)
        c = get_object_or_404(Integrante, pk=codigo)
        e = get_object_or_404(Projeto, nomeProj=c.projeto)
        projeto = str (e.nomeProj)
        area = str (e.area)
        dia = str (d.data)
        mes = str (d.mes)
        ano = str (d.ano)
        p.translate(inch,inch)
        p.setFont("Helvetica", 14)
        p.rotate(90)
        image = os.path.join("Certificado.png") 
        artur = os.path.join("carlos.png") 
        jeff = os.path.join("jeff.png") 
        #p.drawImage(image, -1.0*inch,-550, width=840,height=620)
        p.drawImage(artur, 1*inch,-400, width=91,height=50)
        p.drawImage(jeff, 7*inch,-400, width=180,height=50)
        #p.drawImage(image, -1.0*inch,-550, width=840,height=620)
        p.setFont("Helvetica-BoldOblique", 12)
        p.drawString(1*inch, -220, "Certificamos que " + c.nomeIntegrante + " participou do projeto " + projeto + ", área temática " + area + " ")  
        p.drawString(0.5*inch, -240, "apresentado na FEITEC 2011 – Feira de Ciência Tecnologia e Inovação do IFF – Campus Campos Centro,")
        p.drawString(0.5*inch, -260, " realizada na 19ª Semana do Saber Fazer Saber, nos dias 7,8 e 9 de setembro de 2011.")
        p.setFont("Helvetica-BoldOblique", 12)
        p.drawString(6*inch, -290, "Campos dos Goytacazes, " + dia + " de " + mes + " de " + ano)
        p.setFont("Helvetica-Oblique", 12)        
        p.drawString(0.5*inch, -415, "Carlos Artur de Carvalho Arêas")  
        p.drawString(0.5*inch, -430, "Diretor do Departamento de Desenvolvimento") 
        p.drawString(0.5*inch, -445, "Institucional e Extensão Campus Campos-Centro")
        p.setFont("Helvetica-BoldOblique", 12)
        p.drawString(7*inch, -415, "Jefferson Manhães de Azevedo")  
        p.drawString(7*inch, -430, "Diretor Geral do IFF") 
        p.drawString(7*inch, -445, "Campus Campos-Centro")        
        p.setFont("Helvetica-Oblique", 8)
        p.drawString(8*inch,-490, "O presente certificado foi registrado sob o n." + d.numeroCert)        
        p.drawString(8*inch, -500, "No Livro n. " + d.livroCert + " em " + d.dataCert)
        p.showPage()
        p.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

class ProjetoModelForm(ModelForm):
    class Meta:
        exclude = ('salaProj','blocoProj','enviar')
        model = Projeto
        widgets={
            'criador':HiddenInput(attrs={'size':50}),
            'situacao':HiddenInput(attrs={'size':50}),
            #'salaProj' : HiddenInput(),
            #'blocoProj' : HiddenInput(),
            #'enviar' : HiddenInput(),
        }

class ProfessorModelForm(ModelForm):
    class Meta:
        model = Professor

class IntegranteModelForm(ModelForm):
    class Meta:
        model = Integrante
        widgets={
            'situacaoIntegrante':HiddenInput(attrs={'size':50}),
        }

class DadosCertModelFormIntegrante(ModelForm):
    class Meta:
        model = CertificadoIntegrante
        widgets = {
            'integrante':HiddenInput(),
        }

class DadosCertModelFormProfessor(ModelForm):
    class Meta:
        model = CertificadoProfessor
        widgets = {
            'professor':HiddenInput(),
        }

class ProjetoGerenciaForm(ModelForm):
    class Meta:
        exclude = ('enviar')
        model = Projeto
        widgets = {
            'criador': HiddenInput(attrs={'size':50}),
			'situacao': HiddenInput(attrs={'size':50}),
			'area': HiddenInput(),
			'nomeProj' : HiddenInput(),
			'resumoProj' : HiddenInput(),
			'materialProj' : HiddenInput(),
			'campusProj' : HiddenInput(),
			'equipamentoProj' : HiddenInput(),
            #'enviar' : HiddenInput(),
			
        }

class ProjetoGerenciaModelForm(ModelForm):
    class Meta:
        model = Projeto
        widgets = {
            'criador': HiddenInput(attrs={'size':50}),
			'situacao': HiddenInput(attrs={'size':50}),
			'area': HiddenInput(),
			'nomeProj' : HiddenInput(),
			'resumoProj' : HiddenInput(),
			'materialProj' : HiddenInput(),
			'campusProj' : HiddenInput(),
			'equipamentoProj' : HiddenInput(),
            'enviar' : HiddenInput(),
			
        }

class SituacaoIntModelForm(ModelForm):
	class Meta:	
		model = Integrante
		widgets = {  
            'codIntegrante' : HiddenInput(),        
            'nomeIntegrante': HiddenInput(),
            'cpfIntegrante': HiddenInput(), 
            'matriculaIntegrante' : HiddenInput(),
            'cursoIntegrante': HiddenInput(), 
            'tamanhocamisaIntegrante': HiddenInput(), 
            'projeto': HiddenInput(), 
            'campusIntegrante':HiddenInput(),
			
        }
