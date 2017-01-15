import scrapy

from wow.items import WowItem

class WowSpider( scrapy.Spider ):
    name = "wow"

    def start_requests(self):
        urls = [ 'https://us.battle.net/forums/en/wow/22814056/?page=%i' % i 
                    for i in range(1,10) ]
	for url in urls:
	    yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = WowItem()
        posts = response.xpath('//*[@id="forum-topics"]/div[1]')

        for post in posts:
            # grab all entries on page
            urls = post.xpath('a[@class="ForumTopic"]/@href').extract()
            titles = post.xpath('a[@class="ForumTopic"]/div/span[1]/span/span[2]/text()').extract()
            authors = post.xpath('a[@class="ForumTopic"]/div/span[3]/text()').extract()
            replies = post.xpath('a[@class="ForumTopic"]/div/span[4]/span[1]/text()').extract()
            first_posts = post.xpath('a[@class="ForumTopic"]/div/span[2]/text()').extract()

            # yield single item per entry
            for url, title, author, reply, first_post in zip(urls, titles, authors, replies, first_posts):
                item['url'] = url.strip()
                item['title'] = title.strip()
                item['author'] = author.strip()
                item['replies'] = reply.strip()
                item['first_post'] = first_post.strip()
                yield item

            
