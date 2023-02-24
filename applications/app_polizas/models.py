from django.conf import settings
from django.db import models

from applications.app_domicilio.models import Domicilio
from applications.app_personas.models import Sucursal


class Poliza(models.Model):
    GENDER_TIPO = (
        ("E", "Egreso"),
        ("I", "Ingreso"),
        ("D", "Diario"),
    )
    GENDER_APLICACION = (
        ("N", "Normal"),
        ("C", "Condonacion"),
        ("O", "ChequeOrden"),
        ("D", "CierreDiario"),
        ("M", "CierreMensual"),
        ("A", "CierreAnual"),
    )
    GENDER_FUENTE = (
        ("O", "Operacion"),
        ("A", "Activos"),
        ("N", "Nomina"),
        ("G", "Gastos"),
        ("P", "Pasiva"),
        ("T", "Traslados"),
        ("R", "Traspasos"),
    )
    tipo = models.CharField(
        max_length=1,
        choices=GENDER_TIPO,
        verbose_name="Tipo de poliza",
        default="E",
    )
    numero = models.IntegerField(verbose_name="Número de poliza")
    sucursal = models.ForeignKey(
        Sucursal,
        on_delete=models.PROTECT,
        verbose_name="Sucursal a la que pertenece:",
    )
    fecha = models.DateTimeField(verbose_name="Fecha de poliza")
    fecharegistro = models.DateTimeField(auto_now=True)
    concepto = models.CharField(max_length=200, verbose_name="Concepto de la poliza")
    usuarioElabora = models.IntegerField(verbose_name="Usuario Elabora:")
    usuarioAutoriza = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        verbose_name="Usuario Autoriza:",
    )
    aplicacion = models.CharField(
        max_length=1,
        choices=GENDER_APLICACION,
        default="N",
        verbose_name="Aplicacion de poliza",
    )
    fuente = models.CharField(
        max_length=1,
        choices=GENDER_FUENTE,
        default="O",
        verbose_name="Fuente de poliza",
    )
    automatica = models.BooleanField(verbose_name="Poliza automatica")

    class Meta:
        verbose_name = "Poliza"
        verbose_name_plural = "Polizas"

    def __str__(self):
        return self.tipo + " " + str(self.numero) + " " + self.concepto


class Banco(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre del banco")

    class Meta:
        verbose_name = "Banco"
        verbose_name_plural = "Bancos"

    def __str__(self):
        return self.nombre


class PolizaEgreso(models.Model):
    poliza = models.ForeignKey(Poliza, on_delete=models.CASCADE)
    beneficiario = models.CharField(
        max_length=70, verbose_name="Nombre del beneficiario"
    )
    banco = models.ForeignKey(Banco, on_delete=models.PROTECT)
    cheque = models.CharField(max_length=10, verbose_name="Numero de cheque")

    class Meta:
        verbose_name = "Poliza Egreso"
        verbose_name_plural = "Polizas Egreso"

    def __str__(self):
        return self.beneficiario


class Proveedor(models.Model):
    GENDER_TIPOPROV = (
        ("N", "04 Nacional"),
        ("E", "05 Extranjera"),
        ("G", "15 Glonbal"),
    )

    GENDER_OPERACIONPROV = (
        ("P", "03 Por servicios profesionales"),
        ("A", "06 Arrendamiento"),
        ("O", "85 Otros"),
    )

    nombre = models.CharField(max_length=100, verbose_name="Nombre del proveedor")
    domicilio = models.ForeignKey(Domicilio, on_delete=models.PROTECT)
    rfc = models.CharField(max_length=15, verbose_name="RFC", unique=True)
    curp = models.CharField(max_length=18, verbose_name="CURP")
    telefono = models.CharField(max_length=10, verbose_name="Número de teléfono")
    tipo = models.CharField(
        max_length=1,
        choices=GENDER_TIPOPROV,
        default="N",
        verbose_name="Tipo de proveedor",
    )
    operacion = models.CharField(
        max_length=1,
        choices=GENDER_OPERACIONPROV,
        default="P",
        verbose_name="Operacion de proveedor",
    )
    regimen = models.CharField(max_length=100, verbose_name="Regimen Fiscal")
    nombreExtranjero = models.CharField(max_length=50)
    paisResidencia = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    banco = models.ForeignKey(Banco, on_delete=models.PROTECT)
    cuentaClabe = models.CharField(max_length=25)

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

    def __str__(self):
        return self.nombre


class PolizaSoporte(models.Model):
    poliza = models.ForeignKey(Poliza, on_delete=models.CASCADE)
    gastoacomprobar = models.IntegerField(default=0)
    archivo = models.CharField(max_length=300, blank=True)
    chavecfdi = models.CharField(max_length=100, blank=True)
    subtotal = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    monto = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    descuento = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    impuesto = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    rfc = models.CharField(max_length=15, blank=True)
    polizaSoporteRelacion = models.IntegerField(default=0)

    class Meta:
        verbose_name = "PolizaSoporte"
        verbose_name_plural = "PolizasSoporte"

    def __str__(self):
        return self.poliza + " " + self.polizaSoporteRelacion


class ClaveUnidad(models.Model):
    clave = models.CharField(max_length=8)
    descripcion = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Clave Unidad"
        verbose_name_plural = "Claves Unidad"

    def __str__(self):
        return self.clave + " " + self.descripcion


class DetallePolizaSoporte(models.Model):
    polizaSoporte = models.ForeignKey(PolizaSoporte, on_delete=models.CASCADE)
    claveProdServ = models.CharField(max_length=8)
    cantidad = models.DecimalField(max_digits=12, decimal_places=2)
    claveUnidad = models.ForeignKey(ClaveUnidad, on_delete=models.PROTECT)
    descripcion = models.CharField(max_length=100)
    unitario = models.DecimalField(max_digits=12, decimal_places=2)
    objetoImp = models.CharField(max_length=2)
    base = models.DecimalField(max_digits=12, decimal_places=2)
    impuesto = models.CharField(max_length=3)
    tipoFactor = models.CharField(max_length=20)
    tasaoCuota = models.DecimalField(max_digits=8, decimal_places=6)
    importe = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = "Detalle Poliza Soporte"
        verbose_name_plural = "Detalle Polizas Soporte"

    def __str__(self):
        return self.descripcion


class CatalogoCuenta(models.Model):
    GENDER_CLASIFICACION = (
        ("C", "Capitulo"),
        ("S", "Subn Capitulo"),
        ("M", "Mayor"),
        ("E", "Menor"),
    )
    GENDER_GRUPO = (
        ("A", "Activo"),
        ("P", "Pasivo"),
        ("C", "Capital"),
        ("R", "Resultado Acreedor"),
        ("D", "Resultado Deudor"),
        ("O", "Orden"),
        ("U", "Puente"),
    )
    GENDER_FINALIDAD = (
        ("C", "Caja"),
        ("B", "Banco"),
        ("O", "Otros"),
    )
    GENDER_NATURALEZA = (
        ("A", "Deudora"),
        ("D", "Acreedora"),
    )

    cuenta = models.CharField(max_length=30, verbose_name="Cuenta contable")
    cuentaSiti = models.CharField(max_length=15, verbose_name="Cuenta Siti")
    nombre = models.CharField(max_length=50, verbose_name="Nombre cuenta")
    clasificacion = models.CharField(
        max_length=1,
        choices=GENDER_CLASIFICACION,
        default="C",
        verbose_name="Clasificación contable",
    )
    grupo = models.CharField(
        max_length=1, choices=GENDER_GRUPO, default="A", verbose_name="Grupo contable"
    )
    finalidad = models.CharField(
        max_length=1,
        choices=GENDER_FINALIDAD,
        default="O",
        verbose_name="Finalidad contable",
    )
    naturaleza = models.CharField(
        max_length=1,
        choices=GENDER_NATURALEZA,
        default="A",
        verbose_name="Naturaleza contable",
    )
    afectable = models.BooleanField(default=0, verbose_name="Afectable")
    padre = models.CharField(
        max_length=30, verbose_name="Padre o nivel superior de la cuenta"
    )
    nivel = models.IntegerField()
    balance = models.BooleanField(
        default=0, verbose_name="La cuenta se desplegara en el balance"
    )
    catalogoMinimo = models.BooleanField(
        default=0, verbose_name="Desplegar en el catalogo Minimo"
    )
    nombreBalance = models.CharField(
        max_length=100, verbose_name="Nombre que desplegara en el balance"
    )
    nombreSiti = models.CharField(
        max_length=70, verbose_name="Nombre de la cuenta en el SITI"
    )
    cuentaPadreSiti = models.CharField(
        max_length=15, verbose_name="Padre o nivel superior cuenta SITI"
    )
    cuentaAgrupar = models.CharField(
        max_length=30, verbose_name="Cuenta a la que agrupará"
    )
    ordenSiti = models.IntegerField(
        verbose_name="Orden en que desplegara en la base del SITI"
    )
    subCuentaSiti = models.BooleanField(verbose_name="SubCuenta de catalogo SITI")
    prorrateo = models.BooleanField(default=0)

    class Meta:
        verbose_name = "Catalogo de cuenta"
        verbose_name_plural = "Catalogo de cuentas"

    def __str__(self):
        return self.nombre


class DetallePoliza(models.Model):
    GENDER_TIPOIVA = (
        ("NA", "No aplica"),
        ("16", "16%"),
        ("8", "8%"),
        ("11", "11%"),
        ("0", "0%"),
        ("E", "Excento"),
        ("R", "Retenido"),
    )

    poliza = models.ForeignKey(Poliza, on_delete=models.CASCADE)
    cuenta = models.ForeignKey(CatalogoCuenta, on_delete=models.PROTECT)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.PROTECT)
    cargo = models.DecimalField(max_digits=14, decimal_places=2)
    abono = models.DecimalField(max_digits=14, decimal_places=2)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)
    concepto = models.CharField(max_length=100)
    iva = models.CharField(
        max_length=2, choices=GENDER_TIPOIVA, default="NA", verbose_name="Tasa de IVA"
    )

    class Meta:
        verbose_name = "Detalle Poliza"
        verbose_name_plural = "Detalle Polizas"

    def __str__(self):
        return str(self.cuenta) + " " + str(self.concepto)
