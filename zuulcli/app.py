import sys
import os

from cliff import app
from cliff import commandmanager
import requests
import pkg_resources
import logging

LOG = logging.getLogger(__name__)


class ZuulCli(app.App):
    log = logging.getLogger(__name__)

    def __init__(self):
        dist = pkg_resources.get_distribution('zuulcli')
        super(ZuulCli, self).__init__(
            description='CLI tool for Zuul API',
            version=dist.version,
            command_manager=commandmanager.CommandManager('zuulcli.commands'),
        )
        self.parser.add_argument(
            '--zuul-url',
            default=os.environ.get("ZUUL_URL"),
            help='Zuul url, default as ENV: ZUUL_URL')

    def http_request(self, path, method='GET', **kwargs):
        if not self.options.zuul_url:
            raise Exception("Please specify zuul url with '--zuul-url' or "
                            "env variable: ZUUL_URL")
        url = "%s%s%s" % (self.options.zuul_url, '/api', path)
        resp = requests.request(method, url, **kwargs)
        LOG.debug(resp.json())
        return resp


def main(argv=sys.argv[1:]):
    return ZuulCli().run(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
