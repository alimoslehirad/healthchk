# Toman Helm Chart

This chart contains the needed manifests to deploy Toman backend.

## Prerequisites Details

* Kubernetes 1.11+
* PV dynamic provisioning support on the underlying infrastructure
* Redis
* Postgresql
* A secret containing required environment variables.


## Installing the Chart

To install the chart with the release name `my-release`:

```bash
$ helm install --name my-release helm/toman-staging-dev
```

## Deleting the Charts

Delete the Helm deployment as normal

```
$ helm delete my-release
```



## Configuration

The following table lists the configurable parameters of the toman chart and their default values.

|              Parameter               |                             Description                             |                       Default                       |
| ------------------------------------ | ------------------------------------------------------------------- | --------------------------------------------------- |
| `appVersion`                         | Application Version (Toman)                                 | `22c3def9`                                             |
| `image.repository`                   | Container image name                                                | `registry.hamdocker.ir/qbit/backend` |
| `image.tag`                          | Container image tag                                                 | `22c3def9`                                             |
| `image.pullPolicy`                   | Container pull policy                                               | `Always`                                      |
| `initImage.repository`               | Init container image name                                           | `registry.hamdocker.ir/qbit/backend`                                           |
| `initImage.tag`                      | Init container image tag                                            | `22c3def9`                                            |
| `initImage.pullPolicy`               | Init container pull policy                                          | `Always`                                            |
| `storage.media`                       | Media Storage Name                                        | `media`                                     |
| `storage.statics`                       | Statics Storage Name                                        | `statics`                                     |
| `deployment.replicas`                | Number of replicas  | `3` |
| `deployment.resources`                   | deployment node resources requests & limits                             | `{} - cpu limit must be an integer`                 |
| `deployment.podAnnotations`              | Deployment annotations                                       | `{}`                                                |
| `deployment.nodeSelector`                | Node labels for pod assignment                               | `{}`                                                |
| `deployment.tolerations`                 | deployment tolerations                                                  | `[]`                                                |
| `deployment.antiAffinity`                | deployment anti-affinity policy                                         | `soft`                                              |
| `deployment.nodeAffinity`                | deployment node affinity policy                                         | `{}`                                                |
| `deployment.initResources`               | deployment initContainer resources requests & limits                    | `{}`                                                |
| `podDisruptionBudget.enabled`               | Enable pod disruption budget                    | `true`                                                |
| `podDisruptionBudget.minAvailable`               | minimum number of available pods                    | `2`                                                |
| `podDisruptionBudget.maxUnavailable`               | maximum number of unavailable pods                     | `1`                                                |

