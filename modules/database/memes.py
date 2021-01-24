from get_enviroment import MEMES
from modules.database.decorator import singleton


@singleton
class MemesList:
    def __init__(self):
        self.dict = {}
        for item in MEMES:
            self.dict[item['key']] = {'name': item['name'],
                                      'url': item['blank'][:-4],
                                      'example': item['example'],
                                      'lines': int(item['lines']),
                                      'key': item['key'],
                                      }

    def get_url_meme(self, key):
        meme = self.dict.get(key, None)
        if meme is None:
            return ""
        return meme['url']

    def get_info_all(self):
        result = list(self.dict.values())
        result.sort(key=lambda x: x['name'])
        return result

    def get_info(self, key):
        return self.dict[key]
