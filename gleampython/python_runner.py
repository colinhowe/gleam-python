class Bunch(dict):
    def __init__(self,**kw):
        dict.__init__(self,kw)
        self.__dict__ = self

class Runner(dict):
    def __init__(self):
        self['nodes'] = []
        self.nodes = self['nodes']
        self.current_node = [self]
        self.value = None
        self.macros = Bunch()

    def makeNode(self, name, attrs, value):
        node = {'name': name, 'attrs': attrs, 'nodes': [], 'value': None}
        self.current_node[-1]['nodes'].append(node)
        self.current_node.append(node)
        if callable(value):
            value()
        else:
            node['value'] = value
        self.current_node.pop()

    def addMacro(self, name, macro):
        setattr(self.macros, name, macro)

gleam = Runner()
