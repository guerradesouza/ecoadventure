from django.db import models
import uuid
from stdimage.models import StdImageField

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )
    servico = models.CharField('Serviço', max_length=100)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 400, 'height': 400, 'crop':True}})
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Ícone', max_length=24, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico


class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo

class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb':{'width':480, 'height':480, 'crop':True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome

CURSOS_CHOICES = (
    ('aph', 'Curso APH'),
    ('sbv', 'Curso SBV'),
) 
class InscricaoForm(models.Model):
    nomeCompleto = models.CharField( max_length=100)
    rg = models.CharField( max_length=100)
    cpf = models.CharField(max_length=100)
    dataDeNascimento = models.DateField( blank=False, null=False)
    localOndeTrabalha = models.CharField( max_length=100)
    profissao = models.CharField( max_length=100)
    email = models.EmailField( blank=False, null=False)
    telefone = models.CharField( max_length=20)
    whatsapp = models.CharField( max_length=20)
    facebook = models.CharField( max_length=100)
    instagram = models.CharField( max_length=100)
    cidadeDoCurso = models.CharField( max_length=100)
    endereco = models.CharField( max_length=200)
    curso_escolhido = models.CharField(max_length=3, choices=CURSOS_CHOICES)
    obs = models.TextField()

    def __str__(self):
        return self.nomeCompleto
    



