import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Join, MapCompose
from propiedades.items import PropiedadesItem

## myspider.py

from urllib.parse import urlencode
from scrapingbee import ScrapingBeeClient

API_KEY = 'YOURAPIKEY'

def get_proxy_url(url):
    payload = {'api_key': API_KEY, 'url': url}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url


class PropspiderSpider(scrapy.Spider):
    name = "propspider"
    #allowed_domains = ["inmobusqueda.com.ar"]
    #start_urls = ["https://www.inmobusqueda.com.ar/departamento-venta-ensenada.html?publicado=2"]

   # def __init__(self, *args ,**kwargs):
   #     super(PropspiderSpider, self).__init__(*args, **kwargs)
   #     self.pages_to_scrape = int(kwargs.get('pages', -1))

    def start_requests(self):
        urls = ["https://www.inmobusqueda.com.ar/departamento-venta-la-plata-casco-urbano.html?publicado=4",
                "https://www.inmobusqueda.com.ar/departamento-venta-partido-berisso.html?publicado=4"]
        for url in urls:
            print(url)
            yield scrapy.Request(url=get_proxy_url(url), callback=self.parse)
                                 #meta={"proxy": "https://proxy.scrapeops.io/v1/?api_key=yourapikey"})
                           #meta={"proxy": "http://scraperapi:youapikey@proxy-server.scraperapi.com:8001"})

    def parse(self, response, **kargs):
        contenedor = response.xpath('//div[@class="resultadoContenedorDatosResultados"]')
        for link in contenedor:
            url = link.xpath('.//a/@href').get()
            url_ = get_proxy_url(url)
            direccion = link.xpath('.//a/text()').get()
            precio = link.xpath('.//div[@class="resultadoPrecio "]/text()').get()
            codigo = link.xpath('.//div[@class="rdBox codigo"]/text()').get()
            yield scrapy.Request(url=url_, callback=self.parse_prop, meta={"precio": precio, "codigo": codigo, "direccion": direccion})
                                                                         #"proxy": "https://proxy.scrapeops.io/v1/?api_key=yourapikey"})
                                                                         #"proxy": "http://scraperapi:yourapikey@proxy-server.scraperapi.com:8001"})

        try:
            next_page = response.xpath('//a/font[contains(text(), "Siguiente")]/../@href')[0]
            if next_page:
                url_base =   "https://www.inmobusqueda.com.ar/"
                url_next_page = next_page.get()
                url_next_page = url_base + url_next_page
                url_next_page_final = get_proxy_url(url_next_page)
                print("URL NEXT PAGE", url_next_page_final)
                print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
                yield response.follow(url=url_next_page_final, callback=self.parse)
        except IndexError:
            next_page = None


    def parse_prop(self, response):
        precio = response.meta["precio"]
        codigo = response.meta["codigo"]
        direccion = response.meta["direccion"]

        data_prop_atributes = response.xpath('//div[@class="wrap"]/div[@class="detalleizquierda"]/text()')
        data_prop_results = response.xpath('//div[@class="wrap"]/div[@class="detallederecha colorVerde"]')
        data_prop_more_atributes = response.xpath('//div[@class="wrap"]/div[@class="detallecolDerecha"]/div[@class="detalleizquierda2"]/text()')
        data_prop_more_results = response.xpath('//div[@class="wrap"]/div[@class="detallecolDerecha"]/div[@class="detallederecha2 colorVerde"]')

        data_atributes = data_prop_atributes + data_prop_more_atributes
        data_results = data_prop_results + data_prop_more_results
        data_dict = {}
        for i, element in enumerate(data_atributes):
            text_clean = element.get().strip()
            text_clean =   text_clean.replace(".", "")
            text_clean = text_clean.lower()
            text_clean = text_clean.split(" ")
            text_clean = "_".join(text_clean)
            if data_results[i].xpath('./text()').get() == None:
                res = "No especificado"
            else:
                res = data_results[i].xpath('./text()').get()
            data_dict.update({text_clean: res})

        item = ItemLoader(item=PropiedadesItem(), response=response, selector=response)


        for key, value in data_dict.items():
            item.add_value(key, value)


        item.add_value("precio", precio.strip())
        item.add_value("url", response.url)
        item.add_value('codigo', codigo.strip())
        item.add_value("direccion",direccion)
        item.add_xpath("fecha_actualizacion", './/div[@class="wrapficha"]/div[@class="opcion actualizada "]/text()')


        yield item.load_item()
