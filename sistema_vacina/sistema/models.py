from django.db import models
from django.db.models.fields import BooleanField
from django.db.models.fields.related import OneToOneField

class Paciente (models.Model):
    nome = models.CharField(max_length=20)
    cartao_SUS = models.CharField(unique=True,max_length=15)
    cpf = models.CharField(unique=True, max_length=11)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=60)
    grupos_prioridade_CHOICE = (
        ('1','idoso'),
        ('2','Publico Geral'),
        ('3','Academicos de Saude'),
        ('4','Trabalhadores da linha de frente'),
        ('5','Pessoas com Comorbidade'),
        ('6','Gestantes e Lactantes de 18 a 59')
    ) 
    grupos_Prioridade = models.CharField(max_length=1, choices = grupos_prioridade_CHOICE,default="", editable=True)
    ja_tomou_segunda_dose = BooleanField(default=False)
    
    def __str__(self):
        return self.nome
    
class Enfermeiro(models.Model):
    nome = models.CharField(max_length=20)
    cpf = models.CharField(unique=True, max_length=11)
    coren = models.CharField(unique=True, max_length=12)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=60)
    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome, self.coren

class Vacinas(models.Model):
    vacinas_tipos_CHOICE = (
        ('1','Pfizer'),
        ('2','Sputnik'),
        ('3','AstraZeneca'),
        ('4','CoronaVac')
    ) 
    vacinas = models.CharField(max_length=1, choices=vacinas_tipos_CHOICE)

    def __str__(self):
        return self.vacinas

class Estado(models.Model):
    estados_lista_CHOICE = (
        ('1','Acre (AC)'),
        ('2','Alagoas (AL)'),
        ('3','Amapá (AP)'),
        ('4','Amazonas (AM)'),
        ('5','Bahia (BA)'),
        ('6','Ceará (CE)'),
        ('7','Distrito Federal (DF)'),
        ('8','Espírito Santo (ES)'),
        ('9','Goiás (GO)'),
        ('10','Maranhão (MA)'),
        ('11','Mato Grosso (MT)'),
        ('12','Mato Grosso do Sul (MS)'),
        ('13','Minas Gerais (MG)'),
        ('14','Pará (PA)'),
        ('15','Paraíba (PB)'),
        ('16','Paraná (PR)'),
        ('17','Pernambuco (PE)'),
        ('18','Piauí (PI)'),
        ('19','Rio de Janeiro (RJ)'),
        ('20','Rio Grande do Norte (RN)'),
        ('21','Rio Grande do Sul (RS)'),
        ('22','Rondônia (RO)'),
        ('23','Roraima (RR)'),
        ('24','Santa Catarina (SC)'),
        ('25','São Paulo (SP)'),
        ('26','Sergipe (SE)'),
        ('27','Tocantins (TO)'),
    ) 
    estados = models.CharField(max_length=2, choices=estados_lista_CHOICE)
    
    def __str__(self):
        return self.estados

class Cidade (models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Locais (models.Model):
    nome = models.CharField(max_length=20)
    endereco = models.CharField(max_length=60)
    numero_endereco = models.CharField(unique=True, max_length=4)

    def __str__(self):
        return self.locais