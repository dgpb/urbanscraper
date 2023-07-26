import scrapy
from scrapy.spiders import CrawlSpider, Rule
from ..items import UrbanscraperItem
from scrapy.linkextractors import LinkExtractor



class PropiedadesSpider(CrawlSpider):
    name = 'propiedades'
    allowed_domains = ["todoinmuebles.net"]
    start_urls = ['https://todoinmuebles.net/anuncios/inmuebles']

    rules = (
       Rule(LinkExtractor(allow='inmuebles/'), callback='parse_item'),
    )

    def parse_item(self, response):
        items = UrbanscraperItem()

        title = response.xpath('//*[@id="content"]/div[1]/div/div/article/section[1]/div[3]/h2/text()').extract_first().replace('\n', ' ').strip()
        status = response.xpath('//*[@id="content"]/div[1]/div/div/article/section[1]/div[1]/div[1]/ul/li[1]/span/text()').extract_first().replace('\n', ' ').strip()
        published_date = response.xpath('//*[@id="content"]/div[1]/div/div/article/section[1]/div[1]/div[1]/ul/li[2]/text()').extract_first().replace('\n', ' ').strip()
        views = response.xpath('//*[@id="content"]/div[1]/div/div/article/section[1]/div[1]/div[1]/ul/li[3]/text()').extract_first().replace('\n', ' ').strip()
        type_property = response.xpath('//*[@id="content"]/div[1]/div/div/article/section[1]/div[2]/div[1]/p[3]/text()').extract_first()
        type_transaction = response.xpath('//*[@id="content"]/div[1]/div/div/article/section[1]/div[2]/div[1]/p[1]/text()').extract_first().replace('\n', ' ').strip()
        price_usd = response.xpath('//*[@id="content"]/div[1]/div/div/article/section[1]/div[2]/div[2]/p[2]/text()').extract_first().replace('USD', ' ').strip()
        contact = response.xpath('//*[@id="request-info"]/div/div/div/div/a/text()').extract_first().replace('\n', ' ').strip()
        contact_type = response.xpath('//*[@id="request-info"]/div/div/div/div[2]/p/text()').extract_first()
        url = response.url

        items['title'] = title
        items['status'] = status
        items['published_date'] = published_date
        items['views'] = views
        items['type_property'] = type_property
        items['type_transaction'] = type_transaction
        items['price_usd'] = price_usd
        items['contact'] = contact
        items['contact_type'] = contact_type
        items['url'] = url


        yield items








