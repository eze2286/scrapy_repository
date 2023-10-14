# settings.py

BOT_NAME = "propiedades"

SPIDER_MODULES = ["propiedades.spiders"]
NEWSPIDER_MODULE = "propiedades.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "propiedades (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "propiedades.middlewares.PropiedadesSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "propiedades.middlewares.PropiedadesDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "propiedades.pipelines.PropiedadesPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

# Configure item pipelines

# En este item pipeline se eliminan los duplicados
# Se guarda la data en una base de datos sqlite
# Se guarda la data en una base de datos mongo
# Se aplica una funcion para cuando los precios son None
ITEM_PIPELINES = {
    "propiedades.pipelines.PropiedadesRemoveDuplicatesPipeline": 100,
    "propiedades.pipelines.PropiedadesPrecioNonePipeline": 300,
    #"propiedades.pipelines.SaveDataSqlitePipeline": 400,
    #"propiedades.pipelines.SaveDataMongoPipeline": 200,   
}

# Configuración de la base de datos mongodb
# Recordar instalar pymongo para que esto funcione
MONGO_URI = "mongodb://localhost:27017"
MONGO_DATABASE = "propiedades"

# # Recordar instalar botocore para que esto funcione
# FEEDS = {
#     "s3://scrapy-inmobusqueda/%(name)s/%(name)s_%(time)s.csv" : {
#         "format": "csv",
#         "encoding": "latin1",
#         "store_empty": False,
#     },
# }
# Configuración para el bucket de S3
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''

# Esto es para que scrapy por defecto use un user agent aleatorio
# Recordar instalar scrapy-user-agents para que esto funcione

# Add Your ScrapeOps API Key
SCRAPEOPS_API_KEY = '49c9e3d5-a29a-4a17-ad6b-2e3f5a6a503b'

# Add In The ScrapeOps Extension
EXTENSIONS = {
        'scrapeops_scrapy.extension.ScrapeOpsMonitor': 500, 
        }
DOWNLOADER_MIDDLEWARES = {
    "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
    #"scrapy_user_agents.middlewares.RandomUserAgentMiddleware": 400,
    'scrapeops_scrapy.middleware.retry.RetryMiddleware': 550,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
}

# Configuración del sistema de registro
# LOG_ENABLED = True
# LOG_LEVEL = "INFO"
# LOG_FILE = "propiedades.log"
