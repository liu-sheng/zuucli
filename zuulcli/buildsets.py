import logging

from cliff import lister
from cliff import show

LOG = logging.getLogger(__name__)


class BuildsetList(lister.Lister):
    """show buildsets list info of Zuul.
    """
    headers = ('UUID', 'Project', 'Job Name', 'Result', 'Start Time')
    properties = ('uuid', 'project', 'job_name', 'result', 'start_time')

    headers_long = ('UUID', 'Project', 'Job Name', 'Result', 'Start Time', 'Log Url')
    properties_long = ('uuid', 'project', 'job_name', 'result', 'start_time', 'log_url')

    def get_parser(self, prog_name):
        parser = super(BuildsetList, self).get_parser(prog_name)
        parser.add_argument('--long',
                            action='store_true',
                            help='list zuul buildsets info with more properties',
                            )
        parser.add_argument('--project',
                            help='list zuul buildsets info filtered by project',
                            )
        parser.add_argument('--pipeline',
                            help='list zuul buildsets info filtered by pipeline',
                            )
        parser.add_argument('--change',
                            help='list zuul buildsets info filtered by change',
                            )
        parser.add_argument('--branch',
                            help='list zuul buildsets info filtered by branch',
                            )
        parser.add_argument('--patchset',
                            help='list zuul buildsets info filtered by patchset',
                            )
        parser.add_argument('--ref',
                            help='list zuul buildsets info filtered by ref',
                            )
        parser.add_argument('--newrev',
                            help='list zuul buildsets info filtered by newrev',
                            )
        parser.add_argument('--uuid',
                            help='list zuul buildsets info filtered by uuid',
                            )
        parser.add_argument('--result',
                            help='list zuul buildsets info filtered by result',
                            )
        parser.add_argument('--limit',
                            type=int,
                            help='list zuul buildsets info with limt, default is 50',
                            )
        parser.add_argument('--skip',
                            type=int,
                            help='offset when list query with limit, default is 0',
                            )
        return parser

    def take_action(self, parsed_args):
        if parsed_args.long:
            headers, properties = self.headers_long, self.properties_long
        else:
            headers, properties = self.headers, self.properties
        url = '/buildsets'
        filters = ''
        for filter in ['project', 'pipeline', 'change', 'branch', 'patchset',
                       'ref', 'newrev', 'uuid', 'result', 'limit']:
            if getattr(parsed_args, filter) is not None:
                filters += "%s=%s" % (filter, getattr(parsed_args, filter))
        if filters:
            url += "?%s" % filters
        resp = self.app.http_request(url)
        values = [[b[p] for p in properties] for b in resp.json()]
        return headers, values


class BuildsetShow(show.ShowOne):
    """show one buildset info from Zuul API.
    """

    def get_parser(self, prog_name):
        parser = super(BuildsetShow, self).get_parser(prog_name)
        parser.add_argument('buildset_id',
                            help='specified buildset id to show',
                            )
        return parser

    def take_action(self, parsed_args):
        resp = self.app.http_request('/buildset/%s' % parsed_args.build_id)
        return zip(*sorted(resp.json().items()))
