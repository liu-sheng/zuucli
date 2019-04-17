import logging

from cliff import lister
from cliff import show

LOG = logging.getLogger(__name__)


class BuildsList(lister.Lister):
    """show builds list info of Zuul.
    """
    headers = ('UUID', 'Project', 'Job Name', 'Result', 'Start Time')
    properties = ('uuid', 'project', 'job_name', 'result', 'start_time')

    headers_long = ('UUID', 'Project', 'Job Name', 'Result', 'Start Time', 'Log Url')
    properties_long = ('uuid', 'project', 'job_name', 'result', 'start_time', 'log_url')

    def get_parser(self, prog_name):
        parser = super(BuildsList, self).get_parser(prog_name)
        parser.add_argument('--long',
                            help='list zuul builds info with more properties',
                            )
        return parser

    def take_action(self, parsed_args):
        if parsed_args.long:
            headers, properties = self.headers_long, self.properties_long
        else:
            headers, properties = self.headers, self.properties
        resp = self.app.http_request('/builds')
        values = [[b[p] for p in properties] for b in resp.json()]
        return headers, values


class BuildShow(show.ShowOne):
    """show one build info from Zuul API.
    """

    def get_parser(self, prog_name):
        parser = super(BuildShow, self).get_parser(prog_name)
        parser.add_argument('build_id',
                            help='specified build id to show',
                            )
        return parser

    def take_action(self, parsed_args):
        resp = self.app.http_request('/build/%s' % parsed_args.build_id)
        return zip(*sorted(resp.json().items()))
