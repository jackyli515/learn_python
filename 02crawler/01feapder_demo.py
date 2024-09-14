# https://feapder.com/#/README
# 精简版 pip install feapder    精简版：不支持浏览器渲染、不支持基于内存去重、不支持入库mongo
# 浏览器渲染版 pip install "feapder[render]"   浏览器渲染版：不支持基于内存去重、不支持入库mongo
# 完整版版 pip install "feapder[all]"  完整版：支持所有功能


import feapder


class FirstSpider(feapder.AirSpider):
    def start_requests(self):
        yield feapder.Request("https://news.baidu.com/")

    def parse(self, request, response):
        print(response)
        page_news = response.xpath('//div[@id="pane-news"]/div/ul/li/strong/a')
        print(page_news.getall())
        news_list = page_news.xpath("//a")
        for news in page_news:
            print(news.xpath("/text()").extract_first())
            print("链接：", news.xpath("./@href").extract_first())


if __name__ == "__main__":
    FirstSpider().start()
