#encoding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail, get_connection, EmailMessage

class Choices(models.Model):
    tamanho = (  
        #Banco de Dados, Mostrar ao Usuário
        ('P', 'P'), 
        ('M', 'M'), 
        ('G', 'G'), 
        ('GG', 'GG'), 
        ('XG', 'XG'), 
    ) 

    situacao = (  
        ('Apresentou', 'Apresentou'), 
        ('Nao Apresentou', 'Nao Apresentou'),
    )
    campus = (
        ('IFF','IFF - Centro'),
        ('Guarus','IFF - Guarus'),
        ('Macaé','IFF - Macaé'),
    )

    participacao = (
        ('Professor','Professor'),
        ('Orientador','Orientador'),
        ('Coordenador','Coordenador'),
    )
    dia = (
        (u'01', u'01'),
        (u'02', u'02'),
        (u'03', u'03'),
        (u'04', u'04'),
        (u'05', u'05'),
        (u'06', u'06'),
        (u'07', u'07'),
        (u'08', u'08'),
        (u'09', u'09'),
        (u'10', u'10'),
        (u'11', u'11'),
        (u'12', u'12'),
        (u'13', u'13'),
        (u'14', u'14'),
        (u'15', u'15'),
        (u'16', u'16'),
        (u'17', u'17'),
        (u'18', u'18'),
        (u'19', u'19'),
        (u'20', u'20'),
        (u'21', u'21'),
        (u'22', u'22'),
        (u'23', u'23'),
        (u'24', u'24'),
        (u'25', u'25'),
        (u'26', u'26'),
        (u'27', u'27'),
        (u'28', u'28'),
        (u'29', u'29'),
        (u'30', u'30'),
        (u'31', u'31'),       
    )

    mes = (
        (u'Janeiro', u'Janeiro'),
        (u'Fevereiro', u'Fevereio'),
        (u'Março', u'Março'),
        (u'Abril', u'Abril'),
        (u'Maio', u'Maio'),
        (u'Junho', u'Junho'),
        (u'Julho', u'Julho'),
        (u'Agosto', u'Agosto'),
        (u'Setembro', u'Setembro'),
        (u'Outubro', u'Outubro'),
        (u'Novembro', u'Novembro'),
        (u'Dezembro', u'Dezembro'),
   )
   
    ano = (
        (u'2011', u'2011'),
        (u'2012', u'2012'),
        (u'2013', u'2013'),
    )
    
class Area(models.Model):
    class Meta:
        verbose_name = 'Área'
        verbose_name_plural = 'Áreas'

    codArea = models.AutoField(primary_key=True)
    descricao = models.CharField("Descrição",max_length=50)

    def __unicode__(self):
        return self.descricao

class Campus(models.Model):
    class Meta:
        verbose_name = 'Campus'
        verbose_name_plural = 'Campi'

    codCampus = models.AutoField(primary_key=True)
    descricao = models.CharField("Descrição",max_length=50)

    def __unicode__(self):
        return self.descricao

class Projeto(models.Model):
    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'

    codProj = models.AutoField(primary_key=True)
    nomeProj = models.CharField("Nome do Projeto",max_length=20, blank=True,help_text="Digite um Nome ao seu projeto",unique=True)
    resumoProj = models.TextField("Resumo",max_length=640, blank=True,help_text="Faça um breve resumo de até 640 caracteres do seu projeto")
    materialProj = models.TextField("Material",max_length=640, blank=True,help_text="Material a ser Adquirido para o Projeto")
    blocoProj = models.CharField("Bloco",max_length=20, blank=True,default = "A ser definido")
    salaProj = models.CharField("Sala",max_length=20, blank=True,default = "A ser definido")
    equipamentoProj = models.TextField("Equipamento",max_length=640, blank=True,help_text="Equipamento necessário para o Projeto")
    criador = models.CharField("Criador", max_length=50,blank=True)
    situacao = models.CharField("Situacao", max_length=50, blank=True,default="Nao Apresentou")
    enviar = models.CharField('Enviar?',max_length=10,blank=True,default="Pendente")
    campusProj = models.ForeignKey('Campus')
    area = models.ForeignKey('Area')

    def __unicode__(self):
        return self.nomeProj

    def save(self, *args, **kwargs):
        super(Projeto, self).save(*args, **kwargs)
    ## ENVIA 1 EMAIL SOMENTE SE FOI APROVADO O CADASTRO ##
        if self.situacao == 'Aprovado' and self.enviar == 'Enviar':
           enviar = User.objects.get(username__iexact=self.criador)
           subject = 'Projeto Feitec'
           message = 'O projeto %s foi será no \nBloco: %s \nSala: %s' %(self.nomeProj,self.blocoProj,self.salaProj)
           from_email = ''#email remetente
           connection = get_connection(username = '', password ='')#email e senha de conexão
           send_email = EmailMessage(subject, message , from_email, [enviar.email], connection = connection)
           send_email.content_subtype = "html"
           send_email.send()


        if (self.situacao == 'Aprovado' or self.situacao == 'Reprovado') and self.enviar == 'Pendente':
            enviar = User.objects.get(username__iexact=self.criador)
            subject = 'Projeto Feitec'
            message = 'O projeto %s foi %s!' %(self.nomeProj,self.situacao)
            from_email = ''#email remetente
            connection = get_connection(username = '', password ='')#email e senha de conexão
            send_email = EmailMessage(subject, message , from_email, [enviar.email], connection = connection)
            send_email.content_subtype = "html"
            send_email.send()

        if self.situacao == 'Enviado':
            enviar = User.objects.get(username__iexact=self.criador)
            subject = 'Projeto Feitec'
            message = 'O projeto %s foi enviado com sucesso.  Aguarde a avaliação do próprio' %(self.nomeProj)
            from_email = ''#email remetente
            connection = get_connection(username = '', password ='')#email e senha de conexão
            send_email = EmailMessage(subject, message , from_email, [enviar.email], connection = connection)
            send_email.content_subtype = "html"
            send_email.send()

    
class Professor(models.Model):
    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'

    codProfessor = models.AutoField(primary_key=True)
    nomeProfessor = models.CharField("Nome do Professor",max_length=50, blank=True)
    emailProfessor = models.EmailField("Email",max_length=50, blank=True)
    matriculaProfessor = models.CharField("Matrícula SIAPE",max_length=7, blank=True)
    tipoProfessor = models.CharField('Participação',max_length=50,blank=True,choices=Choices.participacao)
    projeto = models.ForeignKey('Projeto')

    def __unicode__(self):
        return self.nomeProfessor

class Integrante(models.Model):
    class Meta:
        verbose_name = 'Integrante'
        verbose_name_plural = 'Integrantes'

    codIntegrante = models.AutoField(primary_key=True)
    nomeIntegrante = models.CharField("Nome do Integrante",max_length=50, blank=True)
    cpfIntegrante = models.CharField("Cpf", max_length=11, blank=True)
    cursoIntegrante = models.CharField("Curso", max_length=50, blank=True)
    matriculaIntegrante = models.CharField("Matrícula", max_length=15, blank=True)
    campusIntegrante = models.ForeignKey('Campus')
    tamanhocamisaIntegrante = models.CharField("Tamanho da Camisa", max_length=2,blank=True, choices=Choices.tamanho)
    situacaoIntegrante = models.CharField("Situacao", max_length=20, blank=True, choices=Choices.situacao,default="Pendente")
    projeto = models.ForeignKey('Projeto')

    def __unicode__(self):
        return self.nomeIntegrante

class CertificadoIntegrante(models.Model):
    class Meta:
        verbose_name = 'Certificado do Integrante'
        verbose_name_plural = 'Certificados dos Integrantes'

    codCert = models.AutoField(primary_key=True)
    numeroCert= models.CharField("Numero",max_length=10,default = "00",blank=True)
    livroCert= models.CharField("Livro", max_length=10,default = "00",blank=True)
    dataCert= models.CharField("Data", max_length=10,default = "--/--/----",blank=True)
    data = models.CharField("Data", max_length=10, choices = Choices.dia, blank = True)
    mes = models.CharField("Mes", max_length=20, choices = Choices.mes, blank = True)
    ano = models.CharField("Ano", max_length=10, choices = Choices.ano, blank = True)
    integrante = models.ForeignKey('Integrante')

class CertificadoProfessor(models.Model):
    class Meta:
        verbose_name = 'Certificado do Professor'
        verbose_name_plural = 'Certificados dos Professores'

    codCert = models.AutoField(primary_key=True)
    numeroCert= models.CharField("Numero",max_length=10,default = "00",blank=True)
    livroCert= models.CharField("Livro", max_length=10,default = "00",blank=True)
    dataCert= models.CharField("Data", max_length=10,default = "--/--/----",blank=True)
    data = models.CharField("Data", max_length=10, choices = Choices.dia, blank = True)
    mes = models.CharField("Mes", max_length=20, choices = Choices.mes, blank = True)
    ano = models.CharField("Ano", max_length=10, choices = Choices.ano, blank = True)    
    professor = models.ForeignKey('Professor')
	
