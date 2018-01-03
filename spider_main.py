from quora_spider import url_manager, html_downloader, html_parser,\
    txt_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = txt_outputer.TxtOutputer()

    def craw(self, r_url):
        self.urls.add_new_url(r_url)
        count = 1
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d:%s' % (count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 1000:
                    break
                count += 1
            except:
                print 'craw failed'

        self.outputer.output_txt()

if __name__ == '__main__':
    root_url = 'https://www.quora.com/Python-for-Machine-Learning-1'
    spider = SpiderMain()
    spider.craw(root_url)
