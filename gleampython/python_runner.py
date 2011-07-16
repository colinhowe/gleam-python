class Runner(dict):
    def __init__(self):
        self['nodes'] = []
        self.nodes = self['nodes']
        self.current_node = [self]
        self.value = None

    def makeNode(self, name, attrs, value):
        node = {'name': name, 'attrs': attrs, 'nodes': [], 'value': None}
        self.current_node[-1]['nodes'].append(node)
        self.current_node.append(node)
        if callable(value):
            value()
        else:
            node['value'] = value
        self.current_node.pop()

gleam = Runner()
