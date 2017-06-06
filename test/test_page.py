import os

from html.parser import HTMLParser
import unittest

class HTMLParserTagCheck(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = {}

    def handle_starttag(self, tag, attrs):
        if tag not in self.tags:
            self.tags[tag] = 0

        self.tags[tag] += 1

    def has_tag(self, tag, count=1):
        return tag in self.tags and self.tags[tag] > count

class TestHTML(unittest.TestCase):
    def setUp(self):
        self.parser = HTMLParserTagCheck()
        with open('index.html', 'r') as index_file:
            self.parser.feed(index_file.read())

    def tearDown(self):
        pass

    def test_has_p_tag(self):
        self.assertTrue(self.parser.has_tag('p'), 'Missing a paragraph tag')

if __name__ == '__main__':
    unittest.main()
