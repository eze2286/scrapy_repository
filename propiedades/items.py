# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
from scrapy.loader.processors import Join, MapCompose
import re

def not_found_result(value):
    if value == None:
        return "No especificado"
    else:
        return value.strip()

def default_value_if_empty(value, default="-"):
    return value if value else default

def price_process(p):
    text = p.strip().lower()
    if text == "consulte":
        return None
    else:
        patron = r'(\d[\d,.]*)'
        text = text.replace(".", "")
        text = re.search(patron, text)
        if text:
            text = text.group(1)
            text = text.replace(",", ".")
            return text  

def codigo_process(c):
    text = c.strip()
    text = text.split("-")[1].strip()
    return text
    
       



class PropiedadesItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    habitaciones = Field(output_processor=Join())
    baños = Field()
    garage = Field()
    estado = Field()
    superficie_lote = Field()
    superficie_construida = Field()
    tamaño_lote = Field()
    jardin = Field()
    piscina = Field()
    orientación = Field()
    terraza = Field()
    seguridad = Field()
    calefacción = Field()
    luminosidad = Field()
    apto_profesional = Field()
    ubicación_en_planta = Field()
    piso = Field()
    dependencia_de_servicio = Field()
    ambientes = Field()
    patio = Field()
    fot = Field()
    balcón = Field()
    antigüedad = Field()
    apto_banco = Field()
    toilette = Field()
    detalle_del_edificio = Field()
    nro_pisos = Field()
    deptos_por_piso = Field()
    ascensores_priv = Field()
    ascensores_serv = Field()
    servicios = Field()
    gas = Field()
    cloacas = Field()
    agua = Field()
    asfalto = Field()
    energia = Field()
    teléfono = Field()
    cable = Field()
    permite_mascotas = Field()
    acceso_movreducida = Field()
    precio = Field()
    url = Field()
    codigo = Field()
    fecha_actualizacion = Field()
    direccion = Field()

