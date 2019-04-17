import logging

from cliff import lister

LOG = logging.getLogger(__name__)


class BuildsList(lister.Lister):
    """show builds info of Zuul.
    """
    headers = ('Project', 'Job Name', 'Result', 'Start Time')
    properties = ('project', 'job_name', 'result', 'start_time')

    headers_long = ('Project', 'Job Name', 'Result', 'Start Time')
    properties_long = ('project', 'job_name', 'result', 'start_time')

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
        resp = self.app.http_request('/builds', 'GET')
        values = [[b[p] for p in properties] for b in resp.json()]
        return headers, values
