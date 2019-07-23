from django.db import models

# Create your models here.


class Neighborhood(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    # auto update when data is inserted
    create_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = 'Barrio'
        verbose_name_plural = 'Barrios'
        ordering = ('-name',)
        db_table = 'app_neighborhood'

    def __str__(self):
        return self.name


class Leader(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    last_name = models.CharField(max_length=150, null=False, blank=False)
    # auto update when data is inserted
    create_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = 'Lider'
        verbose_name_plural = 'Lideres'
        ordering = ('name',)
        db_table = 'app_leader'

    def __str__(self):
        return self.name


class Person(models.Model):
    # required
    identification = models.CharField('Identificación', max_length=10,
                                      unique=True, null=False, blank=False,
                                      help_text='Identificación unica')
    celphone = models.CharField('Telefono celular', max_length=12, null=False,
                                blank=False)
    phone = models.CharField('Telefono fijo', max_length=12, null=True,
                             blank=True)
    name = models.CharField('Nombres', max_length=150, null=False, blank=False)
    last_name = models.CharField('Apellidos', max_length=150, null=False,
                                 blank=False)

    rh = models.CharField(max_length=3, null=True, blank=True)
    addres = models.CharField('Dirección', max_length=150, null=True,
                              blank=True)
    birthdate = models.DateField('Fecha de cumpleaños', null=True, blank=True)

    # auto update when data is inserted
    create_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    # auto update when data is altered
    update_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    # fecha de reunión
    date_meeting = models.DateTimeField('Fecha y hora de reunión', null=True,
                                        blank=True)
    state = models.BooleanField('Estado', default=False)
    leader = models.ForeignKey(Leader, on_delete=models.PROTECT, null=False,
                               verbose_name="Lider", blank=False)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.PROTECT,
                                     null=True, verbose_name="Barrio",
                                     blank=True)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering = ('-last_name',)
        db_table = 'app_person'

    def __str__(self):
        return f'{self.name} {self.last_name} ({self.identification})'


