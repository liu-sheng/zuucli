import logging

from cliff import lister
from cliff import show

LOG = logging.getLogger(__name__)


class JobsList(lister.Lister):
    """show builds list info of Zuul.
    """
    headers = ('Dame', 'Description', 'Variants')
    properties = ('name', 'description', 'variants')

    def get_parser(self, prog_name):
        parser = super(JobsList, self).get_parser(prog_name)
        parser.add_argument('--long',
                            help='list zuul builds info with more properties',
                            )
        return parser

    def take_action(self, parsed_args):
        url = '/jobs'
        resp = self.app.http_request(url)
        values = [[b.get(p, '') for p in self.properties] for b in resp.json()]
        return self.headers, values


class JobShow(show.ShowOne):
    """show one job info from Zuul API.
    """

    def get_parser(self, prog_name):
        parser = super(JobShow, self).get_parser(prog_name)
        parser.add_argument('job_name',
                            help='specified job name to show',
                            )
        return parser

    def take_action(self, parsed_args):
        resp = self.app.http_request('/job/%s' % parsed_args.job_name)
        return zip(*sorted(resp.json().items()))
