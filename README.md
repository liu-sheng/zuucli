# CLI tool for Zuul API
A CLI tool for retrieving data from the project gating system [Zuul](https://zuul-ci.org/docs/) APIs.

## Zuul Web API

Zuul have provided a set of APIs for retrieving data about `jobs`, `builds`, `projects` etc. All
the available APIs you can find in the [ZuulWebAPI class](https://opendev.org/zuul/zuul/src/commit/dc9347c1223e3c7eb0399889d03c5de9e854a836/zuul/web/__init__.py#L211) code 

- build: /api/tenant/{tenant}/build/{uuid},
- builds: /api/tenant/{tenant}/builds,
- buildset: /api/tenant/{tenant}/buildset/{uuid},
- buildsets: /api/tenant/{tenant}/buildsets,
- config_errors: /api/tenant/{tenant}/config-errors,
- connections: /api/connections,
- console_stream: /api/tenant/{tenant}/console-stream,
- info: /api/info,
- job: /api/tenant/{tenant}/job/{job_name},
- jobs: /api/tenant/{tenant}/jobs,
- key: /api/tenant/{tenant}/key/{project:.*}.pub,
- labels: /api/tenant/{tenant}/labels,
- nodes: /api/tenant/{tenant}/nodes,
- pipelines: /api/tenant/{tenant}/pipelines,
- project: /api/tenant/{tenant}/project/{project:.*},
- project_freeze_jobs: /api/tenant/{tenant}/pipeline/{pipeline}/project/{project:.*}/branch/{branch:.*}/freeze-jobs,
- project_ssh_key: /api/tenant/{tenant}/project-ssh-key/{project:.*}.pub,
- projects: /api/tenant/{tenant}/projects,
- status: /api/tenant/{tenant}/status,
- status_change: /api/tenant/{tenant}/status/change/{change},
- tenant_info: /api/tenant/{tenant}/info,
- tenants: /api/tenants

**NOTE:** because we have host the Zuul web by `apache`, and have the following rewrite rule:
`RewriteRule api/(.*)$ http://localhost:9000/api/tenant/{tenant}/$1 [P,L]` in apache configuration,
it doesn't need to specify `tenant/{tenant}`  in the above APIs request URL.

For example, you can simply use `curl` command to call these APIs(without authentication), 
using following command to retrieving data bout projects from `status.openlabtesting.org`: 

```bash
$ curl http://status.openlabtesting.org/api/projects | python -m json.tool

[
    {
        "canonical_name": "github.com/ansible/ansible",
        "connection_name": "github",
        "name": "ansible/ansible",
        "type": "untrusted"
    },
    {
        "canonical_name": "github.com/apache/spark",
        "connection_name": "github",
        "name": "apache/spark",
        "type": "untrusted"
    },
    {
        "canonical_name": "github.com/cloudfoundry-incubator/bosh-huaweicloud-cpi-release",
        "connection_name": "github",
        "name": "cloudfoundry-incubator/bosh-huaweicloud-cpi-release",
        "type": "untrusted"
    },
    {
        "canonical_name": "github.com/cloudfoundry/bosh-acceptance-tests",
        "connection_name": "github",
        "name": "cloudfoundry/bosh-acceptance-tests",
        "type": "untrusted"
    },
    ...
]
```
## Usages of this CLI tool

You can simply install this tool with command:
```bash
pip install git+https://github.com/liu-sheng/zuulcli
```

This tool is built based on the [cliff](https://docs.openstack.org/cliff) and the commands style is similar to the [OSC](https://docs.openstack.org/python-openstackclient), you can run `zuulctl help` to show all the
available commands and arguments, following are current supported commands(will support more if necessary):
```bash
  zuulctl complete       print bash completion command (cliff)
  zuulctl help           print detailed help for another command (cliff)
  zuulctl build list     show builds list info of Zuul.
  zuulctl build show     show one build info from Zuul API.
  zuulctl job list       show jobs list info of Zuul.
  zuulctl job show       show one job info from Zuul API.
  zuulctl project list   show projects list info of Zuul.
  zuulctl project show   show one project info from Zuul API.
```

For example, retrieving the jobs biulds info:

```bash
$ export ZUUL_URL=http://status.openlabtesting.org
$ zuulctl build list
+----------------------------------+------------------------------------+--------------------------------------------------------------------------------+--------------+---------------------+
| UUID                             | Project                            | Job Name                                                                       | Result       | Start Time          |
+----------------------------------+------------------------------------+--------------------------------------------------------------------------------+--------------+---------------------+
| 34745e2723ad4d048808027e0b650186 | Yikun/arm-openlab-test             | arm-openlab-test                                                               | SUCCESS      | 2019-04-16T08:47:40 |
| ba4b6ebad5f54f9f8a4533a525139459 | Yikun/arm-openlab-test             | arm-openlab-test                                                               | FAILURE      | 2019-04-16T08:37:31 |
| 4f4905b626e442e589030288c09a3341 | Yikun/arm-openlab-test             | arm-openlab-test                                                               | FAILURE      | 2019-04-16T08:29:11 |
| 700d19ca2b504bf9a2e9f5a8aede901c | Yikun/arm-openlab-test             | arm-openlab-test                                                               | SUCCESS      | 2019-04-16T08:00:41 |
| 5bf75491c35d46dca8819363c7704623 | h00130372/charts                   | helm-integration-test-kubeadm-k8s-v1.12.7                                      | SUCCESS      | 2019-04-16T06:32:11 |
| ae779d3bc3234308b802138ce54466db | h00130372/charts                   | helm-integration-test-kubeadm-k8s-v1.14.0                                      | SUCCESS      | 2019-04-16T06:32:48 |
| 7a63b77495ce42afac6c11d8622a3940 | Yikun/hello-openlab                | hello-openlab-test                                                             | SUCCESS      | 2019-04-16T04:03:13 |
...
```
