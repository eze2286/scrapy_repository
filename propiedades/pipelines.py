# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from propiedades.items import PropiedadesItem
import pymongo




import sqlite3


class PropiedadesRemoveDuplicatesPipeline:
    def __init__(self):
        self.codigos_seen = set()
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter['codigo'][0] in self.codigos_seen:
            raise DropItem(f"Duplicate item found: {item}")
        else:
            self.codigos_seen.add(adapter['codigo'][0])            
        return item

class PropiedadesPrecioNonePipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        fields_item = PropiedadesItem()
        list_fields = [field for field in fields_item.fields]
        list_adapter = [field for field in adapter.keys()]
        #print(list_adapter)
        for f in list_fields:
             if f not in list_adapter:
                print("Detect field not in list_fields: ", f)
                adapter.update({f: "-"})                
            #     adapter.update({ad: "-"})           
        return item
        
        # try:
        #     if adapter['precio'] == None:
        #         raise DropItem(f"Item with precio None found: {item}")
        #     else:
        #         return item
        # except KeyError:
        #     raise DropItem(f"Item with KeyError Precio: {item}")

class SaveDataSqlitePipeline:
    def __init__(self) :
        ## Create/Connect to database
        self.con = sqlite3.connect("propiedades.db")

        ## Create cursor
        self.cur = self.con.cursor()

        ## Create propiedades table if none exists
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS propiedades(            
            habitaciones TEXT,
            baños TEXT,
            garage TEXT,
            estado TEXT,
            superficie_lote TEXT,
            superficie_construida TEXT,
            tamaño_lote TEXT,
            jardin TEXT,
            piscina TEXT,
            orientación TEXT,
            terraza TEXT,
            seguridad TEXT,
            calefacción TEXT,
            luminosidad TEXT,
            apto_profesional TEXT,
            ubicación_en_planta TEXT,
            piso TEXT,
            dependencia_de_servicio TEXT,
            ambientes TEXT,
            patio TEXT,
            fot TEXT,
            balcón TEXT,
            antigüedad TEXT,
            apto_banco TEXT,
            toilette TEXT,
            detale_del_edificio TEXT,
            nro_pisos TEXT,
            deptos_por_piso TEXT,
            ascensores_priv TEXT,
            ascensores_serv TEXT,
            servicios TEXT,
            gas TEXT,
            cloacas TEXT,
            agua TEXT,
            asfalto TEXT,
            energia TEXT,
            teléfono TEXT,
            cable TEXT,
            permite_mascotas TEXT,
            acceso_movreducida TEXT,
            precio REAL,
            url TEXT,
            codigo TEXT PRIMARY KEY,
            fecha_actualizacion TEXT,
            direccion TEXT
        )
        """)
    
    def process_item(self, item, spider):
        ## Check to see if text is already in database
        adapter = ItemAdapter(item)
        #self.cur.execute("SELECT * FROM propiedades WHERE (codigo=?) AND ", (adapter['codigo'][0],))
        self.cur.execute("SELECT * FROM propiedades WHERE codigo=? AND precio=? AND fecha_actualizacion=?", 
                    (adapter['codigo'][0], adapter['precio'], adapter['fecha_actualizacion']))
        result = self.cur.fetchone()

        ## If it is in DB, create log message
        if result:
            spider.logger.warn("Item already in database: %s" % adapter['codigo'][0])
        
        ## If text isn't in the DB, insert data
        else:
            ## Define insert statement
            self.cur.execute("""

            INSERT INTO propiedades VALUES(
                ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
            )
            """, (
                adapter['habitaciones'],
                adapter['baños'],
                adapter['garage'],
                adapter['estado'],
                adapter['superficie_lote'],
                adapter['superficie_construida'],
                adapter['tamaño_lote'],
                adapter['jardin'],
                adapter['piscina'],
                adapter['orientación'],
                adapter['terraza'],
                adapter['seguridad'],
                adapter['calefacción'],
                adapter['luminosidad'],
                adapter['apto_profesional'],
                adapter['ubicación_en_planta'],
                adapter['piso'],
                adapter['dependencia_de_servicio'],
                adapter['ambientes'],
                adapter['patio'],
                adapter['fot'],
                adapter['balcón'],
                adapter['antigüedad'],
                adapter['apto_banco'],
                adapter['toilette'],
                adapter['detalle_del_edificio'],
                adapter['nro_pisos'],
                adapter['deptos_por_piso'],
                adapter['ascensores_priv'],
                adapter['ascensores_serv'],
                adapter['servicios'],
                adapter['gas'],
                adapter['cloacas'],
                adapter['agua'],
                adapter['asfalto'],
                adapter['energia'],
                adapter['teléfono'],
                adapter['cable'],
                adapter['permite_mascotas'],
                adapter['acceso_movreducida'],
                adapter['precio'],
                adapter['url'],
                adapter['codigo'][0],
                adapter['fecha_actualizacion'],
                adapter['direccion']
            ))
            ## Commit changes to database
            self.con.commit()

        return item

class SaveDataMongoPipeline:
    collection_name = "propiedades"

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
    
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri= crawler.settings.get("MONGO_URI"),
            mongo_db= crawler.settings.get("MONGO_DATABASE")
        )
    
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
    
    def close_spider(self, spider):
        self.client.close()
    
    def process_item(self, item, spider):       
        self.db[self.collection_name].insert_one(ItemAdapter(item).asdict())
        return item
                
                

        
