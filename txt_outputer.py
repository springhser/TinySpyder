class TxtOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_txt(self):
        # fout = open('output.html', 'w')
        # fout.write('<html>')
        # fout.write('<body>')
        fout = open('output.txt', 'w')
        for data in self.datas:
            fout.write('Url%s\n--------------------------------------------------------\n' % data['url'].encode('utf-8'))
            fout.write('Question_title: %s\n' % data['question_title'].encode('utf-8'))
            fout.write('---------------------------------------------------------------\n')
            fout.write('Question_details:%s\n' % data['question_details'].encode('utf-8'))
            fout.write("\n***************************************************************\n")
            for answer in data['answers_info']:
                fout.write('\nAnswer_name:%s\n ------------------------------------\nAnswer_content:%s\n' %
                           (answer.encode("utf-8"), data['answers_info'][answer].encode("utf-8")))
                fout.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            fout.write("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n\n")
            fout.write("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n")

            fout.write("---------------------------------------------------------------\n")
        # fout.write('<body>')
        # fout.write('</html>')
        fout.close()
