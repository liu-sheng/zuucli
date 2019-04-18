# CLI tool for Zuul API
A CLI tool for retriving data from Zuul API

## Usages

you can simply install this tool with command:
```bash
pip install git+https://github.com/liu-sheng/zuulcli
```

Then, you can use `zuulctl` command with `--zuul-url` or `ZUUL_URL` environment variable
to retrive data from Zuul API, for an example:

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

```

All the available commands, you can use `zuulctl help/-h/--help` to find, and you can also
use `zuulctl help {command}`to get help infomation about a specified command.
