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

    
    
