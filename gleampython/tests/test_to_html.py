from unittest import TestCase

from to_html import HtmlCreator

class TestHtmlCreator(TestCase):
    def test_simple_node(self):
        self.assertEquals(
            '<p>hello</p>',
            HtmlCreator().as_html([{
                'name': 'p',
                'attrs': {},
                'value': 'hello',
                'nodes': [],
        }]))

    def test_node_attrs(self):
        self.assertEquals(
            '<p class="clazz" size="4">hello</p>',
            HtmlCreator().as_html([{
                'name': 'p',
                'attrs': {'size': 4, 'class': 'clazz'},
                'value': 'hello',
                'nodes': [],
        }]))

    def test_br_node(self):
        self.assertEquals(
            '<br />',
            HtmlCreator().as_html([{
                'name': 'br',
                'attrs': {},
                'value': None,
                'nodes': [],
        }]))

    def test_child_nodes(self):
        self.assertEquals(
            '<p><span>hi</span></p>',
            HtmlCreator().as_html([{
                'name': 'p',
                'attrs': {},
                'value': None,
                'nodes': [
                    { 'name': 'span',
                      'attrs': {},
                      'value': 'hi',
                      'nodes': [],
                    }
                ],
        }]))
