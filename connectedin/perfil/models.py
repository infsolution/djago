from django.db import models

class Perfil(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)
    nome_empresa = models.CharField(max_length=255)
    contatos = models.ManyToManyField('self')
    def __str__(self):
        return self.nome
    def convidar(self, perfil_convidado):
        convite = Convite(solicitante=self, convidado=perfil_convidado)
        convite.save()

class Convite(models.Model):
    solicitante = models.ForeignKey(Perfil, related_name='convites_feitos', on_delete=models.CASCADE)
    convidado = models.ForeignKey(Perfil, related_name='convites_recebidos', on_delete=models.CASCADE)
    def aceitar(self):
        self.convidado.contatos.add(self.solicitante)
        self.solicitante.contatos.add(self.convidado)
        self.delete()
