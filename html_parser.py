from bs4 import BeautifulSoup
import re
import urlparse


class HtmlParser(object):
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', class_="question_link")
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}
        res_data['url'] = page_url
        #<span class="rendered_qtext">Python for Machine Learning?</span>
        #<div class="QuestionArea">
        #<span class="rendered_qtext">
        question_title = soup.find('div', class_='QuestionArea').find('span', class_='rendered_qtext')
        res_data['question_title'] = question_title.get_text()
        question_details = soup.find('div', class_='question_details').find('span', class_='rendered_qtext')
        res_data['question_details'] = question_details.get_text()
        answers = soup.find('div', class_="AnswerListDiv").find_all('div', class_="Answer AnswerBase")
        answers_info = {}
        for answer in answers:
            answer_name = answer.find('a', class_="user")
            name = answer_name.get_text()
            print name
            answer_text = answer.find('div', id=re.compile(r".+answer_content"))
            text = answer_text.get_text()
            answers_info[name] = text
        res_data['answers_info'] = answers_info
        return res_data
