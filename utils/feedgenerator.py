from xml.sax.saxutils import XMLGenerator
from django.utils.feedgenerator import Rss201rev2Feed


class SimplerXMLGenerator(XMLGenerator):
    def addQuickElement(self, name, contents=None, attrs=None, escape=False):
        """Convenience method for adding an element with no children"""
        if attrs is None:
            attrs = {}
        self.startElement(name, attrs)
        if contents is not None:
            if escape:
                self.characters(contents)
            else:
                self._write(contents)
        self.endElement(name)


class ExtFeedGenerator(Rss201rev2Feed):
    mime_type = "application/xml; charset=utf-8"

    def write(self, outfile, encoding):
        handler = SimplerXMLGenerator(outfile, encoding)
        handler.startDocument()
        handler.startElement("rss", self.rss_attributes())
        handler.startElement("channel", self.root_attributes())
        self.add_root_elements(handler)
        self.write_items(handler)
        self.endChannelElement(handler)
        handler.endElement("rss")

    def rss_attributes(self):
        attrs = super().rss_attributes()
        attrs["xmlns:content"] = "http://purl.org/rss/1.0/modules/content/"
        attrs["xmlns:media"] = "http://search.yahoo.com/mrss/"
        attrs["xmlns:georss"] = "http://www.georss.org/georss"
        attrs["xmlns:dc"] = "http://purl.org/dc/elements/1.1/"
        return attrs

    def add_item_elements(self, handler, item):
        super().add_item_elements(handler, item)
        if item["content_encoded"] is not None:
            handler.addQuickElement(
                u"content:encoded", item["content_encoded"], escape=False
            )
