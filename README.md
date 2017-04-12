# a-little-spider
spider_main：爬虫总调度程序

url_manager：URL管理器

html_downloader：html网页下载器

html_parser：html网页解析器

html_outputer：html网页输出器

output.html：运行输出的结果，以html代码格式写入html文件中



从文章中的某一个页面，爬取其页面的a标签，用正则匹配将所有爬取的页面中符合http://www.liuchuo.net/articles/形式的链接提取为待爬取的URL，将文章页面的标题h1标签和时间time标签分别存储在data字典的title和time中，将url、title和time以表格形式输出到html页面

