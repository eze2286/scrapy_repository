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
    habitaciones = scrapy.Field(input_processor=MapCompose(not_found_result))
    baños = scrapy.Field(input_processor=MapCompose(not_found_result))
    garage = scrapy.Field(input_processor=MapCompose(not_found_result))
    estado = scrapy.Field(input_processor=MapCompose(not_found_result))
    superficie_lote = scrapy.Field(input_processor=MapCompose(not_found_result))
    superficie_construida = scrapy.Field(input_processor=MapCompose(not_found_result))
    tamaño_lote = scrapy.Field(input_processor=MapCompose(not_found_result))
    jardin = scrapy.Field(input_processor=MapCompose(default_value_if_empty))
    piscina = scrapy.Field(input_processor=MapCompose(not_found_result))
    orientación = scrapy.Field(input_processor=MapCompose(not_found_result))
    terraza = scrapy.Field(input_processor=MapCompose(not_found_result))
    seguridad = scrapy.Field(input_processor=MapCompose(not_found_result))
    calefacción = scrapy.Field(input_processor=MapCompose(not_found_result))
    luminosidad = scrapy.Field(input_processor=MapCompose(not_found_result))
    apto_profesional = scrapy.Field(input_processor=MapCompose(not_found_result))
    ubicación_en_planta = scrapy.Field(input_processor=MapCompose(not_found_result))
    piso = scrapy.Field(input_processor=MapCompose(not_found_result))
    dependencia_de_servicio = scrapy.Field(input_processor=MapCompose(not_found_result))
    ambientes = scrapy.Field(input_processor=MapCompose(not_found_result))
    patio = scrapy.Field(input_processor=MapCompose(not_found_result))
    fot = scrapy.Field(input_processor=MapCompose(not_found_result))
    balcón = scrapy.Field(input_processor=MapCompose(not_found_result))
    antigüedad = scrapy.Field(input_processor=MapCompose(not_found_result))
    apto_banco = scrapy.Field(input_processor=MapCompose(not_found_result))
    toilette = scrapy.Field(input_processor=MapCompose(not_found_result))
    detalle_del_edificio = scrapy.Field(input_processor=MapCompose(not_found_result))
    nro_pisos = scrapy.Field(input_processor=MapCompose(not_found_result))
    deptos_por_piso = scrapy.Field(input_processor=MapCompose(not_found_result))
    ascensores_priv = scrapy.Field(input_processor=MapCompose(not_found_result))
    ascensores_serv = scrapy.Field(input_processor=MapCompose(not_found_result))
    servicios = scrapy.Field(input_processor=MapCompose(not_found_result))
    gas = scrapy.Field(input_processor=MapCompose(not_found_result))
    cloacas = scrapy.Field(input_processor=MapCompose(not_found_result))
    agua = scrapy.Field(input_processor=MapCompose(not_found_result))
    asfalto = scrapy.Field(input_processor=MapCompose(not_found_result))
    energia = scrapy.Field(input_processor=MapCompose(not_found_result))
    teléfono = scrapy.Field(input_processor=MapCompose(not_found_result))
    cable = scrapy.Field(input_processor=MapCompose(not_found_result))
    permite_mascotas = scrapy.Field(input_processor=MapCompose(not_found_result))
    acceso_movreducida = scrapy.Field(input_processor=MapCompose(not_found_result))
    precio = scrapy.Field(input_processor=MapCompose(price_process))
    url = scrapy.Field(input_processor=MapCompose(not_found_result))
    codigo = scrapy.Field(input_processor=MapCompose(codigo_process))
    fecha_actualizacion = scrapy.Field(input_processor=MapCompose(not_found_result))
    direccion = scrapy.Field(input_processor=MapCompose(not_found_result))
    
