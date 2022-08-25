import scrapy


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']

    def start_requests(self):
        books_url = 'https://books.toscrape.com/catalogue/page-{}.html'
        for i in range(1, 51):
            yield scrapy.Request(books_url.format(i))

    def parse(self, response):
        for s in response.xpath('//article'):
            item = {
                'price': s.xpath('.//p[@class="price_color"]/text()').get(),
                'title': s.xpath('.//h3/a/@title').get()
            }
            yield item
