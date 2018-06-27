class Article:
    def __init__(self, article_id, title, url, code):
        self.article_id = article_id
        self.title = title
        self.url = url
        self.code = code

    def __cmp__(self, other):
        if self.__gt__(other):
            return 1
        elif self.__lt__(other):
            return -1
        else:
            return 0

    def __gt__(self, other):
        if self.article_id > other.article_id:
            return True

    def __lt__(self, other):
        if self.article_id < other.article_id:
            return True

    def __eq__(self, other):
        if self.article_id == other.article_id:
            return True
