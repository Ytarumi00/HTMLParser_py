# -*- coding: utf-8 -*- 

import urllib2
from HTMLParser import HTMLParser
import re

URL = ""
COMMENT1 = ""
COMMENT2 = ""
TAG1 = ""
TAG2 = ""

class TestParser(HTMLParser):
    
    class getDataByComment:
        __value = None
        __tag = None
        __comment = None
        __flagActive = True
        __flagComment = False
        __flagGet = False
        
        @property
        def value(self):
          self.__value = None
        
        @value.getter
        def value(self):
          return self.__value
        
        def cheackComment(self, data):
            match = re.search(self.__comment, data)
            if match != None and self.__flagActive == True:
                self.__flagComment = True
        
        def cheackGet(self, tag): 
            if tag == self.__tag:
                if self.__flagComment == True:
                    self.__flagGet = True
                    self.__flagComment = False
        def getValue(self, data):
            if self.__flagGet == True:
                self.__value = data
                print self.__value
                self.__flagGet = False
                self.__flagActive = False
        def __init__(self, comment, tag):
            self.__comment = comment
            self.__tag = tag
        

    myclass1 = getDataByComment(COMMENT1, TAG1)
    myclass2 = getDataByComment(COMMENT2, TAG2)

    def __init__(self):
        HTMLParser.__init__(self)
    
    def handle_data(self, data):
        self.myclass1.getValue(data)
        self.myclass2.getValue(data)
    def handle_starttag(self, tag, attrs):
        self.myclass1.cheackGet(tag)
        self.myclass2.cheackGet(tag)
    def handle_comment(self, data):
        self.myclass1.cheackComment(data)
        self.myclass2.cheackComment(data)

    output = [myclass1, myclass2]
#     output = (myclass1.value, myclass2.value)

if __name__ == "__main__":

    htmldata = urllib2.urlopen(URL)
    
    parser = TestParser()
    parser.feed(htmldata.read())
    
    str = ""
    for i,v  in enumerate(parser.output):
        str +=  v.value + "\t"
        
    print str
    parser.close()
    htmldata.close()
