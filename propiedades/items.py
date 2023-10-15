# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

#from scrapy.item import Item, Field
import scrapy
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
    
       



class PropiedadesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    habitaciones = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    baños = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    garage = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    estado = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    superficie_lote = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    superficie_construida = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    tamaño_lote = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    jardin = scrapy.Field(input_processor=MapCompose(default_value_if_empty), output_processor=Join())
    piscina = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    orientación = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    terraza = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    seguridad = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    calefacción = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    luminosidad = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    apto_profesional = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    ubicación_en_planta = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    piso = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    dependencia_de_servicio = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    ambientes = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    patio = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    fot = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    balcón = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    antigüedad = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    apto_banco = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    toilette = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    detalle_del_edificio = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    nro_pisos = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    deptos_por_piso = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    ascensores_priv = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    ascensores_serv = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    servicios = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    gas = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    cloacas = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    agua = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    asfalto = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    energia = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    teléfono = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    cable = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    permite_mascotas = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    acceso_movreducida = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    precio = scrapy.Field(input_processor=MapCompose(price_process), output_processor=Join())
    url = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    codigo = scrapy.Field(input_processor=MapCompose(codigo_process))
    fecha_actualizacion = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    direccion = scrapy.Field(input_processor=MapCompose(not_found_result), output_processor=Join())

