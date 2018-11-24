import scrapy


class ShopSpider(scrapy.Spider):
    name = 'ShopSpider'
    start_urls = [
        'https://ilounge.ua/products/silicone-case-oem-ultra-violet-iphone-x-kupit'
        # 'https://blog.scrapinghub.com'
    ]

    def parse(self, response):
        for title in response.css('.rightblock>h1'):
            print("__file__={0}, ==> title => {1}".format(__file__, title))
            yield {'title': title.css('h1 ::text').extract_first()}

        # for next_page in response.css('div.prev-post > a'):
        #     yield response.follow(next_page, self.parse)
