import scrapy

class DmozSpider(scrapy.Spider):
	name='dmoz'
	allowed_domains = ['dmoz.org']
	start_urls = [
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
	]

	def parse(self,response):
		'''		filename = response.url.split("/")[-2] + '.html'
		with open(filename,'wb') as f:
			f.write(response.body)
		'''
		desc = []
		for sel in response.xpath('//div[@class="title-and-desc"]'):
			title = sel.xpath('a/div[@class="site-title"]/text()').extract()[0]
			desc = sel.xpath('div[@class="site-descr "]/text()').extract()[0].strip()
			link = sel.xpath('a/@href').extract()[0]

			print title, link , desc