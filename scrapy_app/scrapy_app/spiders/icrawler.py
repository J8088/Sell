# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from ..items import Case


class IcrawlerSpider(CrawlSpider):
    name = 'icrawler'
    download_delay = 0.5

    # allowed_domains = ['https://google.com']

    # rules = (
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )

    def __init__(self, *args, **kwargs):
        # We are going to pass these args from our django view.
        # To make everything dynamic, we need to override them inside __init__ method
        self.url = kwargs.get('url')
        self.domain = kwargs.get('domain')
        self.start_urls = [self.url]
        self.allowed_domains = [self.domain]

        # self.driver = webdriver.Chrome()
        # self.wait = WebDriverWait(self.driver, 2)

        # IcrawlerSpider.rules = [
        #     Rule(LinkExtractor(unique=True), callback='parse_item'),
        # ]
        IcrawlerSpider.rules = []
        super(IcrawlerSpider, self).__init__(*args, **kwargs)

    def parse_item(self, response):
        i = {}
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()

        i['url'] = response.url
        i['name'] = response.xpath('//h1[@class="product-name"]').extract()
        print("__file__={0}, ==> i => {1}".format(__file__, i))

        return i

    # def scroll_until_loaded(self):
    #     print('!!!!scroll_until_loaded')
    #     check_height = self.driver.execute_script("return document.body.scrollHeight;")
    #     while True:
    #         self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #         try:
    #             self.wait.until(
    #                 lambda driver: self.driver.execute_script("return document.body.scrollHeight;") > check_height)
    #             check_height = self.driver.execute_script("return document.body.scrollHeight;")
    #         except TimeoutException:
    #             print("__file__={0}, ==> BREAK => {1}".format(__file__, ''))
    #             break

    def parse(self, response):
        # self.driver.get(response.url)
        # self.scroll_until_loaded()

        item_dict = {}
        # data = response.xpath('//h1[@class="product-name"]').extract()
        data = response.css('div.product-title::text').extract()
        image_urls = response.css('.main-image').xpath('@src').extract_first()

        image_urls = 'http://url' + image_urls

        # cover = response.urljoin(image_urls)

        # case = Case()
        #
        item_dict['name'] = data
        item_dict['image_url'] = image_urls
        item_dict['full_file_name'] = '/media/scraped/img.jpg'
        # item_dict['cover'] = cover

        # items = self.driver.find_elements_by_css_selector(".product-description-main")
        # print("__file__={0}, ==> items => {1}".format(__file__, items))

        # for item in self.driver.find_elements_by_css_selector("div.product-description-main"):
        #     name = item.find_element_by_css_selector("h1.product-name").text
        #     image_urls = item.find_element_by_css_selector(".description-content").text
        #     print("__file__={0}, ==> name => {1}".format(__file__, name))
        #     print("__file__={0}, ==> image_urls => {1}".format(__file__, image_urls))
        #     item_dict['name'] = name
        #     item_dict['img_urls'] = image_urls
        #     # yield item

        return item_dict
