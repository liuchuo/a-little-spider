class HtmlOutputer(object):

    def __init__(self):
        self.data = []

    def collect_data(self, data):
        if data is None:
            return
        self.data.append(data)

    def output_html(self):
        fout = open('output.html', 'w')

        fout.write("<html>\n<head>\n")
        fout.write("<meta charset='utf-8'>\n</head>\n")
        fout.write("<body>\n")
        fout.write("<table>\n")
        for data in self.data:
            fout.write("<tr>\n")
            fout.write("<td>%s</td>\n" % data['url'].encode('utf-8'))
            fout.write("<td>%s</td>\n" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>\n" % data['time'].encode('utf-8'))
            fout.write("</tr>\n")
        fout.write("</table>\n")
        fout.write("</body>\n")
        fout.write("</html>\n")

        fout.close()