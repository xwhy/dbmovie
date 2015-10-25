from scrapy import Spider
from scrapy.selector import Selector
from dbmovie.items import MovieItem
class dbmeiziSpider(Spider):
    name = "dbmovieSpider"
    allowed_domin =["taobao.com"]
    start_urls = [
        "https://dianying.taobao.com/showList.htm?spm=a1z21.3046609.header.4.fckKRJ&n_s=new", 
    ]
    def parse(self, response):
        movieCardResults = Selector(response).xpath('//div[@class="movie-card-wrap"]')
        for movieCard in movieCardResults:
                item = MovieItem()
                item['movieId'] = movieCard.xpath('a[@class="movie-card"]/@href').extract()
                item['movieName'] = movieCard.xpath('a/div/span[@class="bt-l"]/text()').extract()
                item['movieScore'] = movieCard.xpath('a/div/span[@class="bt-r"]/text()').extract()
                item['moviePoster'] = movieCard.xpath('a/div/img/@src').extract()
                yield item