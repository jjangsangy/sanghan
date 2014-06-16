from __future__ import absolute_import
from docutils import nodes
from docutils.parsers.rst import Directive, directives


class GitHubGist(Directive):
    """ Embed GitHub Gist.

        Usage:
          .. gist:: GIST_ID

    """

    required_arguments = 1
    optional_arguments = 1
    option_spec = {'file': directives.unchanged}
    final_argument_whitespace = True
    has_content = False

    def run(self):
        gistID = self.arguments[0].strip()
        embedHTML = ""
        if 'file' in self.options:
            embedHTML = '<script src="https://gist.github.com/%s.js?file=%s"></script>' % \
                (gistID, self.options['file'])
        else:
            embedHTML = '<script src="https://gist.github.com/%s.js"></script>' % gistID

        return [nodes.raw('', embedHTML, format='html')]

def register():
    directives.register_directive('gist', GitHubGist)
