import requests
import re
from bs4 import BeautifulSoup
from article import Article


# csdn上所有PAT甲级的文章
def get_article_list():
    item_list = []
    for i in range(1, 58):
        # 将文章标题保存在h4_list里
        link = "https://blog.csdn.net/liuchuo/article/list/" + str(i)
        r = requests.get(link)
        soup = BeautifulSoup(r.text, "html.parser")
        h4_list = soup.find_all("h4", class_="text-truncate")
        # 遍历h4_list找到所有包含"甲级"但不包含"java"的标题
        for each in h4_list:
            if "乙级" in each.a.text and "java" not in each.a.text.lower():
                re_result = re.findall('[0-9]{4}', each.a.text)
                if re_result:
                    title = each.a.text.strip().lstrip("原").strip()
                    item_list.append(Article(re_result[0], title, each.a['href'], get_article_content(each.a['href'])))
    return item_list


# liuchuo.net上所有PAT甲级的文章
def get_article_list_from_wordpress():
    item_dict = {}
    for i in range(1, 195):
        link = "https://www.liuchuo.net/page/" + str(i)
        r = requests.get(link)
        soup = BeautifulSoup(r.text, "html.parser")
        entry_titles = soup.find_all("h2", class_="entry-title")
        for entry_title in entry_titles:
            if "甲级" in entry_title.a.text and "java" not in entry_title.a.text.lower():
                title = entry_title.a.text.strip()
                re_result = re.findall('[0-9]{4}', title)
                if re_result:
                    item_dict[re_result[0]] = Article(re_result[0], title, entry_title.a['href'],
                                                      get_article_content_from_wordpress(entry_title.a['href']))
    return item_dict


# 获取csdn上的代码片段，并将代码片段的空格去除
def get_article_content(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    try:
        code = soup.find("div", class_="htmledit_views").pre.code.text
        return re.sub("\s", "", code)
    except AttributeError:
        print("1 " + url)

    try:
        code = soup.find("pre", class_="cpp").text
        return re.sub("\s", "", code)
    except AttributeError:
        print()

    code = soup.find("div", class_="htmledit_views").pre.text
    return re.sub("\s", "", code)


# 获取liuchuo.net上的代码片段，并将代码片段的空格去除
def get_article_content_from_wordpress(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    code = soup.find("td", class_="crayon-code").text
    return re.sub("\s", "", code)


# 比较csdn和liuchuo.net代码，将不相同的文章列表输出到markdown文件中
article_list = get_article_list()
article_dict = get_article_list_from_wordpress()
with open("output.md", "w") as file_object:
    file_object.write("| # | CSDN | Blog |\n")
    file_object.write("|:--:|:---:|:---:|\n")
    for article in sorted(article_list):
        try:
            if article.code != article_dict[article.article_id].code:
                file_object.write(
                    "| " + article.article_id + " | [" + article.url + "](" + article.url + ") | [" + article_dict[
                        article.article_id].url + "](" + article_dict[article.article_id].url + ") |")
        except KeyError:
            print("id: " + article.article_id + " not in liuchuo.net")
    file_object.close()
