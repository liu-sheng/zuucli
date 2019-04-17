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
                            action='store_true',
                            help='list zuul builds info with more properties',
                            )
        parser.add_argument('--project',
                            help='list zuul builds info filtered by project',
                            )
        parser.add_argument('--pipeline',
                            help='list zuul builds info filtered by pipeline',
                            )
        parser.add_argument('--change',
                            help='list zuul builds info filtered by change',
                            )
        parser.add_argument('--branch',
                            help='list zuul builds info filtered by branch',
                            )
        parser.add_argument('--patchset',
                            help='list zuul builds info filtered by patchset',
                            )
        parser.add_argument('--ref',
                            help='list zuul builds info filtered by ref',
                            )
        parser.add_argument('--newrev',
                            help='list zuul builds info filtered by newrev',
                            )
        parser.add_argument('--uuid',
                            help='list zuul builds info filtered by uuid',
                            )
        parser.add_argument('--job-name',
                            help='list zuul builds info filtered by job name',
                            )
        parser.add_argument('--voting',
                            help='list zuul builds info filtered by voting',
                            )
        parser.add_argument('--node-name',
                            help='list zuul builds info filtered by node name',
                            )
        parser.add_argument('--result',
                            help='list zuul builds info filtered by result',
                            )
        parser.add_argument('--limit',
                            help='list zuul builds info with limt, default as 50',
                            )
        return parser

    def take_action(self, parsed_args):
        if parsed_args.long:
            headers, properties = self.headers_long, self.properties_long
        else:
            headers, properties = self.headers, self.properties
        url = '/builds'
        filters = ''
        for filter in ['project', 'pipeline', 'change', 'branch', 'patchset',
                       'ref', 'newrev', 'uuid', 'job_name', 'voting', 'node_name',
                       'result', 'limit']:
            if getattr(parsed_args, filter) is not None:
                filters += "%s=%s" % (filter, getattr(parsed_args, filter))
        if filters:
            url += "?%s" % filters
        resp = self.app.http_request(url)
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
