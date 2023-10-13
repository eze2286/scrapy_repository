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
    
       



class Caracteristicas(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    habitaciones = Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    baños = Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    garage = Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    estado = Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    superficie_lote = Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    superficie_construida = Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    tamaño_lote = Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    jardin = Field(input_processor=MapCompose(default_value_if_empty), output_processor=Join())
    piscina = Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    orientación = Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    terraza = Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    seguridad = Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    calefacción = Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    luminosidad = Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    apto_profesional = Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    ubicación_en_planta = Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    piso = Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    dependencia_de_servicio = Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    ambientes = Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    patio = Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    fot = Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    balcón = Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    antigüedad = Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    apto_banco = Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    toilette = Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    detalle_del_edificio = Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    nro_pisos = Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    deptos_por_piso = Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    ascensores_priv = Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    ascensores_serv = Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    servicios = Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    gas = Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    cloacas = Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    agua = Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    asfalto = Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    energia = Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    teléfono = Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    cable = Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    permite_mascotas = Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    acceso_movreducida = Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    precio = Field(input_processor=MapCompose(price_process), output_processor=Join())
    url = Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    codigo = Field(input_processor=MapCompose(codigo_process))
    fecha_actualizacion = Field(input_processor=MapCompose(not_found_result), output_processor=Join())
    direccion = Field(input_processor=MapCompose(not_found_result), output_processor=Join())


class QuoteItem(Item):
    text = Field()
    tags = Field()
    author = Field()
    test = Field()
