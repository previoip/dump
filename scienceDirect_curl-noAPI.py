import json
from os import sep

class SciDirCurl:

    def setURL(self, url):
        self.url = url

    def getJsonData(self):

        from io import BytesIO
        import re, pycurl, certifi

        user_agent = "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.5) Gecko/20091123 Iceweasel/3.5.5 (like Firefox/3.5.5; Debian-3.5.5-1)"
        url = str(self.url)
        buffer = BytesIO()
        
        curl = pycurl.Curl()
        curl.setopt(curl.URL, url)
        curl.setopt(curl.WRITEDATA, buffer)
        curl.setopt(curl.CAINFO, certifi.where())
        curl.setopt(curl.VERBOSE, 0)
        curl.setopt(curl.USERAGENT, user_agent)
        curl.setopt(curl.TIMEOUT, 20)
        curl.perform()
        curl.close()
        
        data = buffer.getvalue().strip()
        try:
            html = data.decode('utf-8')
        except Exception:
            pass
            return

        regops = re.findall("<script type=\"application/json\".*$", html, re.MULTILINE)[0]
        regops = re.sub('<[^>]+>', '', regops)
        jsonData = json.loads(regops)
        print(jsonData)
        
        if jsonData:
            return jsonData
        else:
            return {}

    def parseJSON(self, json: object):
        
        data = json
        temp_authors = []
        temp_meta = []

        dict_abstract = data["abstracts"]
        dict_article = data["article"]
        dict_authors = data["authors"]["content"][0]["$$"]
        try:
            for i in dict_authors:
                if i["#name"] == "author":
                    temp_authors.append([i["$$"][0]["_"], i["$$"][1]["_"]])

            temp_meta = [
                dict_article["title"]["content"][1]["_"], 
                (dict_article["pages"][0]["first-page"], dict_article["pages"][0]["last-page"]), 
                "Vol " + dict_article["vol-first"],
                dict_article["srctitle"],
                dict_article["dates"]["Publication date"]
            ]
        except Exception:
            pass
        finally:
            if temp_meta and dict_abstract and dict_article and dict_authors:
                return [dict_article, dict_authors, temp_meta,dict_abstract]

    def begin(self):
        data = self.getJsonData()
        return self.parseJSON(data)

def main():
    scidir = SciDirCurl()

    # path = 'urllists.txt'
    # with open(path, 'r', encoding='utf-8') as file:
    #     urls = file.read()
    #     file.close()
    
    url = 'https://www.sciencedirect.com/science/article/pii/S223878542100380X'
    scidir.setURL(url)
    result = scidir.begin()


if __name__ == '__main__':
    main()