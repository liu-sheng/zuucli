import logging

from cliff import lister
from cliff import show

LOG = logging.getLogger(__name__)


class ProjectsList(lister.Lister):
    """show projects list info of Zuul.
    """
    headers = ('Name', 'Canonical Name', 'Type')
    properties = ('name', 'canonical_name', 'type')

    def take_action(self, parsed_args):

        url = '/projects'
        resp = self.app.http_request(url)
        values = [[b.get(p, '') for p in self.properties] for b in resp.json()]
        return self.headers, values


class ProjectShow(show.ShowOne):
    """show one project info from Zuul API.
    """

    def get_parser(self, prog_name):
        parser = super(ProjectShow, self).get_parser(prog_name)
        parser.add_argument('project',
                            help='specified project name to show',
                            )
        return parser

    def take_action(self, parsed_args):
        resp = self.app.http_request('/project/%s' % parsed_args.project)
        return zip(*sorted(resp.json().items()))
