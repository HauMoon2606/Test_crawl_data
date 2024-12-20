import scrapy


class AudibleSpider(scrapy.Spider):
    name = "audible"
    allowed_domains = ["www.audible.com"]
    # start_urls = ["https://www.audible.com/search"]

    def start_requests(self):
        yield scrapy.Request(url="https://www.audible.com/search",callback=self.parse, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'} )
    def parse(self, response):
        products = response.xpath('//*[@id="center-3"]/div/div//li[contains(@class, "productListItem")]')
        for product in products:
            book_title = product.xpath('.//h3[contains(@class,"bc-heading")]/a/text()').get()
            book_author = product.xpath('.//li[contains(@class,"authorLabel")]/span/a/text()').getall()
            book_length = product.xpath('.//li[contains(@class,"runtimeLabel")]/span/text()').get()

            yield{
                "book_title":book_title,
                "book_author":book_author,
                "book_length":book_length
            }

        paging = response.xpath('//ul[contains(@class,"pagingElements")]')
        next_page_url = paging.xpath('.//span[contains(@class,"nextButton")]/a/@href').get()

        if next_page_url:
            yield response.follow(url = next_page_url, callback=self.parse, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'})