
from django.db import models

class Ansiedad(models.Model):
    idansiedad = models.AutoField(primary_key=True)
    idusuarios = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='idusuarios', blank=True, null=True)
    dolordecabeza = models.IntegerField(blank=True, null=True)
    ganasdecomer = models.IntegerField(blank=True, null=True)
    cuestatrabajodormir = models.IntegerField(blank=True, null=True)
    asustaconfacilidad = models.IntegerField(blank=True, null=True)
    sufredetemblor = models.IntegerField(blank=True, null=True)
    sesientenervioso = models.IntegerField(blank=True, null=True)
    sufremaladigestion = models.IntegerField(blank=True, null=True)
    dificlpensarconclaridad = models.IntegerField(blank=True, null=True)
    sesientetriste = models.IntegerField(blank=True, null=True)
    lloraconfrecuencia = models.IntegerField(blank=True, null=True)
    tienedificultaddesuacdiarias = models.IntegerField(blank=True, null=True)
    dificultadtomardesiciones = models.IntegerField(blank=True, null=True)
    dificultadparahacertrabajo = models.IntegerField(blank=True, null=True)
    dificildesempenarpapel = models.IntegerField(blank=True, null=True)
    perdidointeresencosas = models.IntegerField(blank=True, null=True)
    sientepersonainutil = models.IntegerField(blank=True, null=True)
    hatenidoideadeacabarconsuvida = models.IntegerField(blank=True, null=True)
    sesientecansado = models.IntegerField(blank=True, null=True)
    tienesensacionesdesagradables = models.IntegerField(blank=True, null=True)
    secansaconfacilidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ansiedad'


class Datospersonales(models.Model):
    iddatospersonales = models.AutoField(primary_key=True)
    idusuarios = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='idusuarios', blank=True, null=True)
    nombre = models.CharField(max_length=50, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    sexo = models.CharField(max_length=10, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    estadocivil = models.CharField(max_length=20, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    fechanacimiento = models.DateField(blank=True, null=True)
    codigo = models.IntegerField(blank=True, null=True)
    gradoinstruccion = models.CharField(max_length=50, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    ocupacion = models.CharField(max_length=50, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    anodeingreso = models.IntegerField(blank=True, null=True)
    facultadoescuela = models.CharField(max_length=100, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    direccionactual = models.CharField(max_length=100, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    numerocel = models.CharField(max_length=15, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    vivecon = models.CharField(max_length=50, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    numerohermanos = models.IntegerField(blank=True, null=True)
    familiarresponsable = models.CharField(max_length=50, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    numerocelresponsable = models.CharField(max_length=15, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    religion = models.CharField(max_length=50, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datospersonales'


class Psicosis(models.Model):
    idpsicosis = models.AutoField(primary_key=True)
    idusuarios = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='idusuarios', blank=True, null=True)
    sientealherir = models.IntegerField(blank=True, null=True)
    esunapersonaimportante = models.IntegerField(blank=True, null=True)
    hanotadointerferencia = models.IntegerField(blank=True, null=True)
    oyevoces = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'psicosis'


class Usuarios(models.Model):
    idusuarios = models.AutoField(primary_key=True)
    username = models.CharField(max_length=10, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    password = models.CharField(max_length=100, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'