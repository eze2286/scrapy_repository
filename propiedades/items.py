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
    habitaciones = Field(input_processor=MapCompose(not_found_result))
    baños = Field(input_processor=MapCompose(not_found_result))
    garage = Field(input_processor=MapCompose(not_found_result))
    estado = Field(input_processor=MapCompose(not_found_result))
    superficie_lote = Field(input_processor=MapCompose(not_found_result))
    superficie_construida = Field(input_processor=MapCompose(not_found_result))
    tamaño_lote = Field(input_processor=MapCompose(not_found_result))
    jardin = Field(input_processor=MapCompose(default_value_if_empty))
    piscina = Field(input_processor=MapCompose(not_found_result))
    orientación = Field(input_processor=MapCompose(not_found_result))
    terraza = Field(input_processor=MapCompose(not_found_result))
    seguridad = Field(input_processor=MapCompose(not_found_result))
    calefacción = Field(input_processor=MapCompose(not_found_result))
    luminosidad = Field(input_processor=MapCompose(not_found_result))
    apto_profesional = Field(input_processor=MapCompose(not_found_result))
    ubicación_en_planta = Field(input_processor=MapCompose(not_found_result))
    piso = Field(input_processor=MapCompose(not_found_result))
    dependencia_de_servicio = Field(input_processor=MapCompose(not_found_result))
    ambientes = Field(input_processor=MapCompose(not_found_result))
    patio = Field(input_processor=MapCompose(not_found_result))
    fot = Field(input_processor=MapCompose(not_found_result))
    balcón = Field(input_processor=MapCompose(not_found_result))
    antigüedad = Field(input_processor=MapCompose(not_found_result))
    apto_banco = Field(input_processor=MapCompose(not_found_result))
    toilette = Field(input_processor=MapCompose(not_found_result))
    detalle_del_edificio = Field(input_processor=MapCompose(not_found_result))
    nro_pisos = Field(input_processor=MapCompose(not_found_result))
    deptos_por_piso = Field(input_processor=MapCompose(not_found_result))
    ascensores_priv = Field(input_processor=MapCompose(not_found_result))
    ascensores_serv = Field(input_processor=MapCompose(not_found_result))
    servicios = Field(input_processor=MapCompose(not_found_result))
    gas = Field(input_processor=MapCompose(not_found_result))
    cloacas = Field(input_processor=MapCompose(not_found_result))
    agua = Field(input_processor=MapCompose(not_found_result))
    asfalto = Field(input_processor=MapCompose(not_found_result))
    energia = Field(input_processor=MapCompose(not_found_result))
    teléfono = Field(input_processor=MapCompose(not_found_result))
    cable = Field(input_processor=MapCompose(not_found_result))
    permite_mascotas = Field(input_processor=MapCompose(not_found_result))
    acceso_movreducida = Field(input_processor=MapCompose(not_found_result))
    precio = Field(input_processor=MapCompose(price_process))
    url = Field(input_processor=MapCompose(not_found_result))
    codigo = Field(input_processor=MapCompose(codigo_process))
    fecha_actualizacion = Field(input_processor=MapCompose(not_found_result))
    direccion = Field(input_processor=MapCompose(not_found_result))

    
    
