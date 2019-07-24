from django.db import models


class laptop(models.Model):
    modelo = models.CharField(max_length=50)
    precio = models.IntegerField()
    color = models.CharField(max_length=50)
    peso = models.IntegerField()
    procesador = models.CharField(max_length=50)
    ram = models.CharField(max_length=50)

    def __str__(self):
        return "{} ID: {}".format(self.modelo, self.pk)


class camara(models.Model):
    tipo = [
        ('digital', 'Digital'),
        ('reflex', 'Reflex'),
    ]
    modelo = models.CharField(max_length=50)
    precio = models.IntegerField()
    color = models.CharField(max_length=50)
    peso = models.IntegerField()
    tipo = models.CharField(max_length=8, choices=tipo, default='digital')
    megapixeles = models.CharField(max_length=50)

    def __str__(self):
        return "{} ID: {}".format(self.modelo, self.pk)


class minicomponente(models.Model):
    modelo = models.CharField(max_length=50)
    precio = models.IntegerField()
    color = models.CharField(max_length=50)
    peso = models.IntegerField()
    potencia = models.CharField(max_length=50)
    repro_usb = models.BooleanField()

    def __str__(self):
        return "{} ID: {}".format(self.modelo, self.pk)


class carrito(models.Model):
    latops = models.ManyToManyField(laptop)
    camaras = models.ManyToManyField(camara)
    minicomponentes = models.ManyToManyField(minicomponente)

    def __str__(self):
        return "Numero de orden: {}".format(self.pk)
