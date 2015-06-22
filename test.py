# coding=utf-8
import unittest

import main


class TestLab1(unittest.TestCase):

    def test_getAllGeoFromSite(self):
        site = '<html>\n' \
               '<body>\n' \
               'Київ столиця України. Львів - душа України.\n' \
               '</body>\n' \
               '</html>'

        import os

        if os.path.isfile("test.html"):
            os.remove("test.html")

        file = open("test.html", "w")
        file.write(site)
        file.flush()
        file.close()

        actual = main.getAllGeosFromSite("test.html")
        expected = [('Київ', 1), ('Львів', 1)]

        os.remove("test.html")
        self.assertEqual(actual, expected)

    def test_getUrlsFromXml(self):
        data = "<?xml version=\"1.0\"?>" \
               "<data>" \
               "    <url>url1</url>" \
               "    <url>url2</url>" \
               "</data>"

        import os

        if os.path.isfile("test.xml"):
            os.remove("test.xml")

        file = open("test.xml", "w")
        file.write(data)
        file.flush()
        file.close()

        actual = main.getUrlsFromXml("test.xml")
        expected = [u'url1', u'url2']

        os.remove("test.xml")

        self.assertEqual(actual, expected)

    def test_translit(self):
        actual = main.translit("Київ Львів Севастополь")
        expected = "kyyiv lviv sevastopol"

        self.assertEqual(actual, expected)

    def test_run(self):
        main.run()
        actual = True
        try:
            main.run(infile="")
            actual = False
        except Exception:
            actual = True

        expected = True

        self.assertEqual(actual, expected)

    def test_runGevent(self):
        main.runGevent()
        actual = True
        try:
            main.runGevent(infile="")
            actual = False
        except Exception:
            actual = True

        expected = True

        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
