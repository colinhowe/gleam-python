SHORT_TAGS = set(['br'])

class HtmlCreator(object):
    '''Creates HTML from a list of nodes.
    '''
    def as_html(self, nodes):
        result = ''
        for node in nodes:
            attrs = ''
            for attr in node['attrs'].items():
                attrs += ' %s="%s"' % attr

            if node['nodes']:
                value = self.as_html(node['nodes'])
            else:
                value = node['value'] or ''

            if node['name'] in SHORT_TAGS and value == '':
                result += '<%s%s />' % (node['name'], attrs)
            else:
                result += '<%s%s>%s</%s>' % (node['name'], attrs, value, node['name'])
            pass
        return result
