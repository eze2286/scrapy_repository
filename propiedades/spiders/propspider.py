import scrapy


class PropspiderSpider(scrapy.Spider):
    name = "propspider"
    allowed_domains = ["inmobusqueda.com.ar"]
    start_urls = ["https://inmobusqueda.com.ar/departamento-venta-la-plata-casco-urbano.html"]

    def parse(self, response):
        #contenedor_links = response.xpath('//div[@class="resultadoContenedorDatosResultados"]//a/@href')
        #contenedor = response.xpath('//div[@class="resultadoContenedorDatosResultados"]//div[@class="resultadoPrecio "]/text()')
        contenedor = response.xpath('//div[@class="resultadoContenedorDatosResultados"]')
        for link in contenedor:
            #url = link.get()
            url = link.xpath('.//a/@href').get()
            precio = link.xpath('.//div[@class="resultadoPrecio "]/text()').get()
            # print(url)
            yield scrapy.Request(url=url, callback=self.parse_prop, meta={"precio": precio})

        next_page = response.xpath('//a/font[contains(text(), "Siguiente")]/../@href')[0]
        if next_page:
            url_next_page = next_page.get()
            print(url)
            yield response.follow(url=url_next_page, callback=self.parse)
        
    def parse_prop(self, response):
        # data_prop_atributes = response.xpath('//div[@class="wrap"]/div[@class="detalleizquierda"]/text()')
        # data_prop_results = response.xpath('//div[@class="wrap"]/div[@class="detallederecha colorVerde"]/text()')
        # data_prop_more_atributes = response.xpath('//div[@class="wrap"]/div[@class="detallecolDerecha"]/div[@class="detalleizquierda2"]/text()')
        # data_prop_more_results = response.xpath('//div[@class="wrap"]/div[@class="detallecolDerecha"]/div[@class="detallederecha2 colorVerde"]/text()')
        
        precio = response.meta["precio"]

        data_prop_atributes = response.xpath('//div[@class="wrap"]/div[@class="detalleizquierda"]/text()')
        data_prop_results = response.xpath('//div[@class="wrap"]/div[@class="detallederecha colorVerde"]')
        data_prop_more_atributes = response.xpath('//div[@class="wrap"]/div[@class="detallecolDerecha"]/div[@class="detalleizquierda2"]/text()')
        


        list_atributes = []
        list_results = []
        for element in data_prop_atributes:
            list_atributes.append(element.get())
        for result in data_prop_results:
            if result.xpath('./text()').get() == None:
                list_results.append("No especificado")
            else:          
                list_results.append(result.xpath('./text()').get())        
        for element2 in data_prop_more_atributes:
            list_atributes.append(element2.get())        
        for result2 in data_prop_more_results:
            if result2.xpath('./text()').get() == None:
                list_results.append("No especificado")
            else:
                list_results.append(result2.xpath('./text()').get())
        dict_data_prop = dict(zip(list_atributes, list_results))
        #dict_data_prop.update({"precio": response.xpath('//div[@class="subtextosobreslide "]/text()[2]').get() .strip()})
        dict_data_prop.update({"precio": precio.strip()})
        dict_data_prop.update({"url": response.url})
        dict_data_prop.update({"codigo": response.xpath('//div[@class="wrapficha"]/div[@class="opcion codigoanuncio"]/text()').get()})
        dict_data_prop.update({"fecha_actualizacion": response.xpath('//div[@class="wrapficha"]/div[@class="opcion actualizada "]/text()').get()})
        
        yield(dict_data_prop)
