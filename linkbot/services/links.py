class LinkService(object):
    
    def __init__(self, dao):
        self.dao = dao

    def recent(self, count=5):
        return self.dao.recent(count)

    def get_links_with_tag(self, tag=None):
        return self.dao.get_links_with_tag(tag)

    def add_link(self, url, tags=None):
        self.dao.add_link(url, tags)