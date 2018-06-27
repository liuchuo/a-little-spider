# a-little-spider
此文件共两个项目，demo2和spider。demo2是我维护博客过程中帮助自己减轻工作量而写的一个爬虫程序，spider项目为python爬虫的一个小练习。

### demo2

由于我的csdn博客和liuchuo.net博客上有一些代码并不对应，所以写了一个爬虫查找所有不对应的博客文章并输出markdown表格。

##### 主要功能：

1. 爬取csdn上所有PAT甲级的文章，并将结果返回在item_list

2. 爬取liuchuo.net上所有PAT甲级的文章，并将结果返回在item_dict

3. 获取csdn博客上所有PAT甲级文章的代码片段，并将代码中的空格去除

4. 获取liuchuo.net上所有PAT甲级文章的代码片段，并将代码中的空格去除

5. 比较csdn和liuchuo.net的代码，将代码不相同的文章列表用markdown语法以表格的形式输出到outpud.md文件中

   （乙级同理，只需将代码中的关键词“甲级”改为“乙级”）

##### 文件解释：

spider_main.py：爬虫总调度程序

article.py：Article类，包括题解id、标题、URL和代码

output.md：输出的markdown格式的表格文件



### spider

##### 主要功能：

从文章中的某一个页面，爬取其页面的a标签，用正则匹配将所有爬取的页面中符合http://www.liuchuo.net/articles/  形式的链接提取为待爬取的URL，将文章页面的标题h1标签和时间time标签分别存储在data字典的title和time中，将url、title和time以表格形式输出到html页面

##### 文件解释：

spider_main：爬虫总调度程序

url_manager：URL管理器

html_downloader：html网页下载器

html_parser：html网页解析器

html_outputer：html网页输出器

output.html：运行输出的结果，以html代码格式写入html文件中
