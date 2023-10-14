# settings.py

BOT_NAME = 'propiedades'

SPIDER_MODULES = ['propiedades.spiders']
NEWSPIDER_MODULE = 'propiedades.spiders'

# Add Your ScrapeOps API Key
SCRAPEOPS_API_KEY = 'YOUR_API_KEY'

# Add In The ScrapeOps Extension
EXTENSIONS = {
        'scrapeops_scrapy.extension.ScrapeOpsMonitor': 500, 
        }

# Update The Download Middlewares
DOWNLOADER_MIDDLEWARES = {
'scrapeops_scrapy.middleware.retry.RetryMiddleware': 550,
'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
}

