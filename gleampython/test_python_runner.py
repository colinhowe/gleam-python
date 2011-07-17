from unittest import TestCase

from python_runner import Runner

class TestRunner(TestCase):
    def test_make_node_simple(self):
        runner = Runner()
        runner.makeNode('span', {}, 'hello')
        self.assertEquals([
            {'name': 'span',
             'attrs': {},
             'value': 'hello',
             'nodes': []
            }
        ], runner.nodes)

    def test_make_node_block(self):
        runner = Runner()
        def block():
            runner.makeNode('span', {}, 'hello')
        runner.makeNode('p', {}, block)
        self.assertEquals([
            {'name': 'p',
             'attrs': {},
             'value': None,
             'nodes': [
                 {'name': 'span',
                  'attrs': {},
                  'value': 'hello',
                  'nodes': []
                 }
              ]
            }
        ], runner.nodes)

