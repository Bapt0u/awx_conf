# awx_conf
Temp awx conf from awx operator

```bash
➜  awx kubectl get pods -n awx -o jsonpath="{.items[*].spec}" | jq
{
  "containers": [
    {
      "args": [
        "--secure-listen-address=0.0.0.0:8443",
        "--upstream=http://127.0.0.1:8080/",
        "--logtostderr=true",
        "--v=0"
      ],
      "image": "gcr.io/kubebuilder/kube-rbac-proxy:v0.14.1",
      "imagePullPolicy": "IfNotPresent",
      "name": "kube-rbac-proxy",
      "ports": [
        {
          "containerPort": 8443,
          "name": "https",
          "protocol": "TCP"
        }
      ],
      "resources": {
        "limits": {
          "cpu": "500m",
          "memory": "128Mi"
        },
        "requests": {
          "cpu": "5m",
          "memory": "64Mi"
        }
      },
      "securityContext": {
        "allowPrivilegeEscalation": false,
        "capabilities": {
          "drop": [
            "ALL"
          ]
        }
      },
      "terminationMessagePath": "/dev/termination-log",
      "terminationMessagePolicy": "File",
      "volumeMounts": [
        {
          "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
          "name": "kube-api-access-chkdw",
          "readOnly": true
        }
      ]
    },
    {
      "args": [
        "--health-probe-bind-address=:6789",
        "--metrics-bind-address=127.0.0.1:8080",
        "--leader-elect",
        "--leader-election-id=awx-operator"
      ],
      "env": [
        {
          "name": "ANSIBLE_GATHERING",
          "value": "explicit"
        },
        {
          "name": "ANSIBLE_DEBUG_LOGS",
          "value": "false"
        },
        {
          "name": "WATCH_NAMESPACE",
          "valueFrom": {
            "fieldRef": {
              "apiVersion": "v1",
              "fieldPath": "metadata.namespace"
            }
          }
        }
      ],
      "image": "quay.io/ansible/awx-operator:2.17.0",
      "imagePullPolicy": "IfNotPresent",
      "livenessProbe": {
        "failureThreshold": 3,
        "httpGet": {
          "path": "/healthz",
          "port": 6789,
          "scheme": "HTTP"
        },
        "initialDelaySeconds": 15,
        "periodSeconds": 20,
        "successThreshold": 1,
        "timeoutSeconds": 1
      },
      "name": "awx-manager",
      "readinessProbe": {
        "failureThreshold": 3,
        "httpGet": {
          "path": "/readyz",
          "port": 6789,
          "scheme": "HTTP"
        },
        "initialDelaySeconds": 5,
        "periodSeconds": 10,
        "successThreshold": 1,
        "timeoutSeconds": 1
      },
      "resources": {
        "limits": {
          "cpu": "2",
          "memory": "4Gi"
        },
        "requests": {
          "cpu": "50m",
          "memory": "32Mi"
        }
      },
      "securityContext": {
        "allowPrivilegeEscalation": false,
        "capabilities": {
          "drop": [
            "ALL"
          ]
        }
      },
      "terminationMessagePath": "/dev/termination-log",
      "terminationMessagePolicy": "File",
      "volumeMounts": [
        {
          "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
          "name": "kube-api-access-chkdw",
          "readOnly": true
        }
      ]
    }
  ],
  "dnsPolicy": "ClusterFirst",
  "enableServiceLinks": true,
  "imagePullSecrets": [
    {
      "name": "redhat-operators-pull-secret"
    }
  ],
  "nodeName": "minikube",
  "preemptionPolicy": "PreemptLowerPriority",
  "priority": 0,
  "restartPolicy": "Always",
  "schedulerName": "default-scheduler",
  "securityContext": {
    "runAsNonRoot": true
  },
  "serviceAccount": "awx-operator-controller-manager",
  "serviceAccountName": "awx-operator-controller-manager",
  "terminationGracePeriodSeconds": 10,
  "tolerations": [
    {
      "effect": "NoExecute",
      "key": "node.kubernetes.io/not-ready",
      "operator": "Exists",
      "tolerationSeconds": 300
    },
    {
      "effect": "NoExecute",
      "key": "node.kubernetes.io/unreachable",
      "operator": "Exists",
      "tolerationSeconds": 300
    }
  ],
  "volumes": [
    {
      "name": "kube-api-access-chkdw",
      "projected": {
        "defaultMode": 420,
        "sources": [
          {
            "serviceAccountToken": {
              "expirationSeconds": 3607,
              "path": "token"
            }
          },
          {
            "configMap": {
              "items": [
                {
                  "key": "ca.crt",
                  "path": "ca.crt"
                }
              ],
              "name": "kube-root-ca.crt"
            }
          },
          {
            "downwardAPI": {
              "items": [
                {
                  "fieldRef": {
                    "apiVersion": "v1",
                    "fieldPath": "metadata.namespace"
                  },
                  "path": "namespace"
                }
              ]
            }
          }
        ]
      }
    }
  ]
}
{
  "containers": [
    {
      "env": [
        {
          "name": "POSTGRESQL_DATABASE",
          "valueFrom": {
            "secretKeyRef": {
              "key": "database",
              "name": "awx-postgres-configuration"
            }
          }
        },
        {
          "name": "POSTGRESQL_USER",
          "valueFrom": {
            "secretKeyRef": {
              "key": "username",
              "name": "awx-postgres-configuration"
            }
          }
        },
        {
          "name": "POSTGRESQL_PASSWORD",
          "valueFrom": {
            "secretKeyRef": {
              "key": "password",
              "name": "awx-postgres-configuration"
            }
          }
        },
        {
          "name": "POSTGRES_DB",
          "valueFrom": {
            "secretKeyRef": {
              "key": "database",
              "name": "awx-postgres-configuration"
            }
          }
        },
        {
          "name": "POSTGRES_USER",
          "valueFrom": {
            "secretKeyRef": {
              "key": "username",
              "name": "awx-postgres-configuration"
            }
          }
        },
        {
          "name": "POSTGRES_PASSWORD",
          "valueFrom": {
            "secretKeyRef": {
              "key": "password",
              "name": "awx-postgres-configuration"
            }
          }
        },
        {
          "name": "PGDATA",
          "value": "/var/lib/pgsql/data/userdata"
        },
        {
          "name": "POSTGRES_INITDB_ARGS",
          "value": "--auth-host=scram-sha-256"
        },
        {
          "name": "POSTGRES_HOST_AUTH_METHOD",
          "value": "scram-sha-256"
        }
      ],
      "image": "quay.io/sclorg/postgresql-15-c9s:latest",
      "imagePullPolicy": "IfNotPresent",
      "name": "postgres",
      "ports": [
        {
          "containerPort": 5432,
          "name": "postgres-15",
          "protocol": "TCP"
        }
      ],
      "resources": {
        "requests": {
          "cpu": "10m",
          "memory": "64Mi"
        }
      },
      "terminationMessagePath": "/dev/termination-log",
      "terminationMessagePolicy": "File",
      "volumeMounts": [
        {
          "mountPath": "/var/lib/pgsql/data",
          "name": "postgres-15",
          "subPath": "data"
        },
        {
          "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
          "name": "kube-api-access-nvbdv",
          "readOnly": true
        }
      ]
    }
  ],
  "dnsPolicy": "ClusterFirst",
  "enableServiceLinks": true,
  "hostname": "awx-postgres-15-0",
  "nodeName": "minikube",
  "preemptionPolicy": "PreemptLowerPriority",
  "priority": 0,
  "restartPolicy": "Always",
  "schedulerName": "default-scheduler",
  "securityContext": {},
  "serviceAccount": "default",
  "serviceAccountName": "default",
  "subdomain": "awx",
  "terminationGracePeriodSeconds": 30,
  "tolerations": [
    {
      "effect": "NoExecute",
      "key": "node.kubernetes.io/not-ready",
      "operator": "Exists",
      "tolerationSeconds": 300
    },
    {
      "effect": "NoExecute",
      "key": "node.kubernetes.io/unreachable",
      "operator": "Exists",
      "tolerationSeconds": 300
    }
  ],
  "volumes": [
    {
      "name": "postgres-15",
      "persistentVolumeClaim": {
        "claimName": "postgres-15-awx-postgres-15-0"
      }
    },
    {
      "name": "kube-api-access-nvbdv",
      "projected": {
        "defaultMode": 420,
        "sources": [
          {
            "serviceAccountToken": {
              "expirationSeconds": 3607,
              "path": "token"
            }
          },
          {
            "configMap": {
              "items": [
                {
                  "key": "ca.crt",
                  "path": "ca.crt"
                }
              ],
              "name": "kube-root-ca.crt"
            }
          },
          {
            "downwardAPI": {
              "items": [
                {
                  "fieldRef": {
                    "apiVersion": "v1",
                    "fieldPath": "metadata.namespace"
                  },
                  "path": "namespace"
                }
              ]
            }
          }
        ]
      }
    }
  ]
}
{
  "containers": [
    {
      "args": [
        "redis-server",
        "/etc/redis.conf"
      ],
      "image": "docker.io/redis:7",
      "imagePullPolicy": "IfNotPresent",
      "name": "redis",
      "resources": {
        "requests": {
          "cpu": "50m",
          "memory": "64Mi"
        }
      },
      "terminationMessagePath": "/dev/termination-log",
      "terminationMessagePolicy": "File",
      "volumeMounts": [
        {
          "mountPath": "/etc/redis.conf",
          "name": "awx-redis-config",
          "readOnly": true,
          "subPath": "redis.conf"
        },
        {
          "mountPath": "/var/run/redis",
          "name": "awx-redis-socket"
        },
        {
          "mountPath": "/data",
          "name": "awx-redis-data"
        },
        {
          "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
          "name": "kube-api-access-jldc5",
          "readOnly": true
        }
      ]
    },
    {
      "args": [
        "/usr/bin/launch_awx_task.sh"
      ],
      "env": [
        {
          "name": "AWX_COMPONENT",
          "value": "task"
        },
        {
          "name": "SUPERVISOR_CONFIG_PATH",
          "value": "/etc/supervisord_task.conf"
        },
        {
          "name": "AWX_SKIP_MIGRATIONS",
          "value": "1"
        },
        {
          "name": "MY_POD_UID",
          "valueFrom": {
            "fieldRef": {
              "apiVersion": "v1",
              "fieldPath": "metadata.uid"
            }
          }
        },
        {
          "name": "MY_POD_IP",
          "valueFrom": {
            "fieldRef": {
              "apiVersion": "v1",
              "fieldPath": "status.podIP"
            }
          }
        },
        {
          "name": "MY_POD_NAMESPACE",
          "valueFrom": {
            "fieldRef": {
              "apiVersion": "v1",
              "fieldPath": "metadata.namespace"
            }
          }
        }
      ],
      "image": "quay.io/ansible/awx:24.4.0",
      "imagePullPolicy": "IfNotPresent",
      "name": "awx-task",
      "resources": {
        "requests": {
          "cpu": "100m",
          "memory": "128Mi"
        }
      },
      "terminationMessagePath": "/dev/termination-log",
      "terminationMessagePolicy": "File",
      "volumeMounts": [
        {
          "mountPath": "/etc/tower/conf.d/execution_environments.py",
          "name": "awx-application-credentials",
          "readOnly": true,
          "subPath": "execution_environments.py"
        },
        {
          "mountPath": "/etc/tower/conf.d/credentials.py",
          "name": "awx-application-credentials",
          "readOnly": true,
          "subPath": "credentials.py"
        },
        {
          "mountPath": "/etc/tower/conf.d/ldap.py",
          "name": "awx-application-credentials",
          "readOnly": true,
          "subPath": "ldap.py"
        },
        {
          "mountPath": "/etc/tower/SECRET_KEY",
          "name": "awx-secret-key",
          "readOnly": true,
          "subPath": "SECRET_KEY"
        },
        {
          "mountPath": "/etc/tower/settings.py",
          "name": "awx-settings",
          "readOnly": true,
          "subPath": "settings.py"
        },
        {
          "mountPath": "/var/run/redis",
          "name": "awx-redis-socket"
        },
        {
          "mountPath": "/var/run/awx-rsyslog",
          "name": "rsyslog-socket"
        },
        {
          "mountPath": "/etc/receptor/",
          "name": "awx-receptor-config"
        },
        {
          "mountPath": "/etc/receptor/work_private_key.pem",
          "name": "awx-receptor-work-signing",
          "readOnly": true,
          "subPath": "work-private-key.pem"
        },
        {
          "mountPath": "/var/run/receptor",
          "name": "receptor-socket"
        },
        {
          "mountPath": "/var/lib/awx/projects",
          "name": "awx-projects"
        },
        {
          "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
          "name": "kube-api-access-jldc5",
          "readOnly": true
        }
      ]
    },
    {
      "args": [
        "/bin/sh",
        "-c",
        "if [ ! -f /etc/receptor/receptor.conf ]; then\n  cp /etc/receptor/receptor-default.conf /etc/receptor/receptor.conf\n  sed -i \"s/HOSTNAME/$HOSTNAME/g\" /etc/receptor/receptor.conf\nfi\nexec receptor --config /etc/receptor/receptor.conf\n"
      ],
      "image": "quay.io/ansible/awx-ee:24.4.0",
      "imagePullPolicy": "IfNotPresent",
      "name": "awx-ee",
      "resources": {
        "requests": {
          "cpu": "100m",
          "memory": "64Mi"
        }
      },
      "terminationMessagePath": "/dev/termination-log",
      "terminationMessagePolicy": "File",
      "volumeMounts": [
        {
          "mountPath": "/etc/receptor/receptor-default.conf",
          "name": "awx-default-receptor-config",
          "subPath": "receptor.conf"
        },
        {
          "mountPath": "/etc/receptor/",
          "name": "awx-receptor-config"
        },
        {
          "mountPath": "/etc/receptor/tls/ca/mesh-CA.crt",
          "name": "awx-receptor-ca",
          "readOnly": true,
          "subPath": "tls.crt"
        },
        {
          "mountPath": "/etc/receptor/work_private_key.pem",
          "name": "awx-receptor-work-signing",
          "readOnly": true,
          "subPath": "work-private-key.pem"
        },
        {
          "mountPath": "/etc/receptor/tls/",
          "name": "awx-receptor-tls"
        },
        {
          "mountPath": "/var/run/receptor",
          "name": "receptor-socket"
        },
        {
          "mountPath": "/var/lib/awx/projects",
          "name": "awx-projects"
        },
        {
          "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
          "name": "kube-api-access-jldc5",
          "readOnly": true
        }
      ]
    },
    {
      "args": [
        "/usr/bin/launch_awx_rsyslog.sh"
      ],
      "env": [
        {
          "name": "SUPERVISOR_CONFIG_PATH",
          "value": "/etc/supervisord_rsyslog.conf"
        }
      ],
      "image": "quay.io/ansible/awx:24.4.0",
      "imagePullPolicy": "IfNotPresent",
      "name": "awx-rsyslog",
      "resources": {
        "requests": {
          "cpu": "100m",
          "memory": "128Mi"
        }
      },
      "terminationMessagePath": "/dev/termination-log",
      "terminationMessagePolicy": "File",
      "volumeMounts": [
        {
          "mountPath": "/etc/tower/conf.d/credentials.py",
          "name": "awx-application-credentials",
          "readOnly": true,
          "subPath": "credentials.py"
        },
        {
          "mountPath": "/etc/tower/SECRET_KEY",
          "name": "awx-secret-key",
          "readOnly": true,
          "subPath": "SECRET_KEY"
        },
        {
          "mountPath": "/etc/tower/settings.py",
          "name": "awx-settings",
          "readOnly": true,
          "subPath": "settings.py"
        },
        {
          "mountPath": "/var/run/redis",
          "name": "awx-redis-socket"
        },
        {
          "mountPath": "/var/run/awx-rsyslog",
          "name": "rsyslog-socket"
        },
        {
          "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
          "name": "kube-api-access-jldc5",
          "readOnly": true
        }
      ]
    }
  ],
  "dnsPolicy": "ClusterFirst",
  "enableServiceLinks": true,
  "initContainers": [
    {
      "command": [
        "/bin/sh",
        "-c",
        "wait-for-migrations"
      ],
      "image": "quay.io/ansible/awx:24.4.0",
      "imagePullPolicy": "IfNotPresent",
      "name": "init-database",
      "resources": {
        "requests": {
          "cpu": "100m",
          "memory": "128Mi"
        }
      },
      "terminationMessagePath": "/dev/termination-log",
      "terminationMessagePolicy": "File",
      "volumeMounts": [
        {
          "mountPath": "/etc/tower/conf.d/credentials.py",
          "name": "awx-application-credentials",
          "readOnly": true,
          "subPath": "credentials.py"
        },
        {
          "mountPath": "/etc/tower/SECRET_KEY",
          "name": "awx-secret-key",
          "readOnly": true,
          "subPath": "SECRET_KEY"
        },
        {
          "mountPath": "/etc/tower/settings.py",
          "name": "awx-settings",
          "readOnly": true,
          "subPath": "settings.py"
        },
        {
          "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
          "name": "kube-api-access-jldc5",
          "readOnly": true
        }
      ]
    },
    {
      "command": [
        "/bin/sh",
        "-c",
        "hostname=$MY_POD_NAME\nreceptor --cert-makereq \\\n  bits=2048 \\\n  commonname=$hostname \\\n  dnsname=$hostname \\\n  nodeid=$hostname \\\n  outreq=/etc/receptor/tls/receptor.req \\\n  outkey=/etc/receptor/tls/receptor.key\nreceptor --cert-signreq \\\n  req=/etc/receptor/tls/receptor.req \\\n  cacert=/etc/receptor/tls/ca/mesh-CA.crt \\\n  cakey=/etc/receptor/tls/ca/mesh-CA.key \\\n  outcert=/etc/receptor/tls/receptor.crt \\\n  notafter=$(date --iso-8601=seconds --utc --date \"10 years\") \\\n  verify=yes\n"
      ],
      "env": [
        {
          "name": "MY_POD_NAME",
          "valueFrom": {
            "fieldRef": {
              "apiVersion": "v1",
              "fieldPath": "metadata.name"
            }
          }
        }
      ],
      "image": "quay.io/ansible/awx-ee:24.4.0",
      "imagePullPolicy": "IfNotPresent",
      "name": "init-receptor",
      "resources": {
        "requests": {
          "cpu": "100m",
          "memory": "128Mi"
        }
      },
      "terminationMessagePath": "/dev/termination-log",
      "terminationMessagePolicy": "File",
      "volumeMounts": [
        {
          "mountPath": "/etc/receptor/tls/ca/mesh-CA.crt",
          "name": "awx-receptor-ca",
          "readOnly": true,
          "subPath": "tls.crt"
        },
        {
          "mountPath": "/etc/receptor/tls/ca/mesh-CA.key",
          "name": "awx-receptor-ca",
          "readOnly": true,
          "subPath": "tls.key"
        },
        {
          "mountPath": "/etc/receptor/tls/",
          "name": "awx-receptor-tls"
        },
        {
          "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
          "name": "kube-api-access-jldc5",
          "readOnly": true
        }
      ]
    }
  ],
  "nodeName": "minikube",
  "preemptionPolicy": "PreemptLowerPriority",
  "priority": 0,
  "restartPolicy": "Always",
  "schedulerName": "default-scheduler",
  "securityContext": {},
  "serviceAccount": "awx",
  "serviceAccountName": "awx",
  "terminationGracePeriodSeconds": 30,
  "tolerations": [
    {
      "effect": "NoExecute",
      "key": "node.kubernetes.io/not-ready",
      "operator": "Exists",
      "tolerationSeconds": 300
    },
    {
      "effect": "NoExecute",
      "key": "node.kubernetes.io/unreachable",
      "operator": "Exists",
      "tolerationSeconds": 300
    }
  ],
  "volumes": [
    {
      "name": "awx-application-credentials",
      "secret": {
        "defaultMode": 420,
        "items": [
          {
            "key": "credentials.py",
            "path": "credentials.py"
          },
          {
            "key": "ldap.py",
            "path": "ldap.py"
          },
          {
            "key": "execution_environments.py",
            "path": "execution_environments.py"
          }
        ],
        "secretName": "awx-app-credentials"
      }
    },
    {
      "emptyDir": {},
      "name": "awx-receptor-tls"
    },
    {
      "name": "awx-receptor-ca",
      "secret": {
        "defaultMode": 420,
        "secretName": "awx-receptor-ca"
      }
    },
    {
      "name": "awx-receptor-work-signing",
      "secret": {
        "defaultMode": 420,
        "secretName": "awx-receptor-work-signing"
      }
    },
    {
      "name": "awx-secret-key",
      "secret": {
        "defaultMode": 420,
        "items": [
          {
            "key": "secret_key",
            "path": "SECRET_KEY"
          }
        ],
        "secretName": "awx-secret-key"
      }
    },
    {
      "configMap": {
        "defaultMode": 420,
        "items": [
          {
            "key": "settings",
            "path": "settings.py"
          }
        ],
        "name": "awx-awx-configmap"
      },
      "name": "awx-settings"
    },
    {
      "configMap": {
        "defaultMode": 420,
        "items": [
          {
            "key": "nginx_conf",
            "path": "nginx.conf"
          }
        ],
        "name": "awx-awx-configmap"
      },
      "name": "awx-nginx-conf"
    },
    {
      "configMap": {
        "defaultMode": 420,
        "items": [
          {
            "key": "redis_conf",
            "path": "redis.conf"
          }
        ],
        "name": "awx-awx-configmap"
      },
      "name": "awx-redis-config"
    },
    {
      "emptyDir": {},
      "name": "awx-redis-socket"
    },
    {
      "emptyDir": {},
      "name": "awx-redis-data"
    },
    {
      "emptyDir": {},
      "name": "rsyslog-socket"
    },
    {
      "emptyDir": {},
      "name": "receptor-socket"
    },
    {
      "emptyDir": {},
      "name": "awx-receptor-config"
    },
    {
      "configMap": {
        "defaultMode": 420,
        "items": [
          {
            "key": "receptor_conf",
            "path": "receptor.conf"
          }
        ],
        "name": "awx-awx-configmap"
      },
      "name": "awx-default-receptor-config"
    },
    {
      "emptyDir": {},
      "name": "awx-projects"
    },
    {
      "name": "kube-api-access-jldc5",
      "projected": {
        "defaultMode": 420,
        "sources": [
          {
            "serviceAccountToken": {
              "expirationSeconds": 3607,
              "path": "token"
            }
          },
          {
            "configMap": {
              "items": [
                {
                  "key": "ca.crt",
                  "path": "ca.crt"
                }
              ],
              "name": "kube-root-ca.crt"
            }
          },
          {
            "downwardAPI": {
              "items": [
                {
                  "fieldRef": {
                    "apiVersion": "v1",
                    "fieldPath": "metadata.namespace"
                  },
                  "path": "namespace"
                }
              ]
            }
          }
        ]
      }
    }
  ]
}
{
  "containers": [
    {
      "args": [
        "redis-server",
        "/etc/redis.conf"
      ],
      "image": "docker.io/redis:7",
      "imagePullPolicy": "IfNotPresent",
      "name": "redis",
      "resources": {
        "requests": {
          "cpu": "50m",
          "memory": "64Mi"
        }
      },
      "terminationMessagePath": "/dev/termination-log",
      "terminationMessagePolicy": "File",
      "volumeMounts": [
        {
          "mountPath": "/etc/redis.conf",
          "name": "awx-redis-config",
          "readOnly": true,
          "subPath": "redis.conf"
        },
        {
          "mountPath": "/var/run/redis",
          "name": "awx-redis-socket"
        },
        {
          "mountPath": "/data",
          "name": "awx-redis-data"
        },
        {
          "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
          "name": "kube-api-access-j9sbr",
          "readOnly": true
        }
      ]
    },
    {
      "args": [
        "/usr/bin/launch_awx_web.sh"
      ],
      "env": [
        {
          "name": "AWX_COMPONENT",
          "value": "web"
        },
        {
          "name": "SUPERVISOR_CONFIG_PATH",
          "value": "/etc/supervisord_web.conf"
        },
        {
          "name": "MY_POD_NAMESPACE",
          "valueFrom": {
            "fieldRef": {
              "apiVersion": "v1",
              "fieldPath": "metadata.namespace"
            }
          }
        },
        {
          "name": "MY_POD_IP",
          "valueFrom": {
            "fieldRef": {
              "apiVersion": "v1",
              "fieldPath": "status.podIP"
            }
          }
        },
        {
          "name": "UWSGI_MOUNT_PATH",
          "value": "/"
        }
      ],
      "image": "quay.io/ansible/awx:24.4.0",
      "imagePullPolicy": "IfNotPresent",
      "name": "awx-web",
      "ports": [
        {
          "containerPort": 8052,
          "protocol": "TCP"
        }
      ],
      "resources": {
        "requests": {
          "cpu": "100m",
          "memory": "128Mi"
        }
      },
      "terminationMessagePath": "/dev/termination-log",
      "terminationMessagePolicy": "File",
      "volumeMounts": [
        {
          "mountPath": "/etc/tower/uwsgi.ini",
          "name": "awx-uwsgi-config",
          "readOnly": true,
          "subPath": "uwsgi.conf"
        },
        {
          "mountPath": "/etc/tower/conf.d/execution_environments.py",
          "name": "awx-application-credentials",
          "readOnly": true,
          "subPath": "execution_environments.py"
        },
        {
          "mountPath": "/etc/tower/conf.d/credentials.py",
          "name": "awx-application-credentials",
          "readOnly": true,
          "subPath": "credentials.py"
        },
        {
          "mountPath": "/etc/tower/conf.d/ldap.py",
          "name": "awx-application-credentials",
          "readOnly": true,
          "subPath": "ldap.py"
        },
        {
          "mountPath": "/etc/tower/SECRET_KEY",
          "name": "awx-secret-key",
          "readOnly": true,
          "subPath": "SECRET_KEY"
        },
        {
          "mountPath": "/etc/tower/settings.py",
          "name": "awx-settings",
          "readOnly": true,
          "subPath": "settings.py"
        },
        {
          "mountPath": "/etc/nginx/nginx.conf",
          "name": "awx-nginx-conf",
          "readOnly": true,
          "subPath": "nginx.conf"
        },
        {
          "mountPath": "/var/run/redis",
          "name": "awx-redis-socket"
        },
        {
          "mountPath": "/var/run/awx-rsyslog",
          "name": "rsyslog-socket"
        },
        {
          "mountPath": "/etc/receptor/tls/ca/mesh-CA.crt",
          "name": "awx-receptor-ca",
          "readOnly": true,
          "subPath": "tls.crt"
        },
        {
          "mountPath": "/etc/receptor/tls/ca/mesh-CA.key",
          "name": "awx-receptor-ca",
          "readOnly": true,
          "subPath": "tls.key"
        },
        {
          "mountPath": "/etc/receptor/work_public_key.pem",
          "name": "awx-receptor-work-signing",
          "readOnly": true,
          "subPath": "work-public-key.pem"
        },
        {
          "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
          "name": "kube-api-access-j9sbr",
          "readOnly": true
        }
      ]
    },
    {
      "args": [
        "/usr/bin/launch_awx_rsyslog.sh"
      ],
      "env": [
        {
          "name": "SUPERVISOR_CONFIG_PATH",
          "value": "/etc/supervisord_rsyslog.conf"
        }
      ],
      "image": "quay.io/ansible/awx:24.4.0",
      "imagePullPolicy": "IfNotPresent",
      "name": "awx-rsyslog",
      "resources": {
        "requests": {
          "cpu": "100m",
          "memory": "128Mi"
        }
      },
      "terminationMessagePath": "/dev/termination-log",
      "terminationMessagePolicy": "File",
      "volumeMounts": [
        {
          "mountPath": "/etc/tower/conf.d/credentials.py",
          "name": "awx-application-credentials",
          "readOnly": true,
          "subPath": "credentials.py"
        },
        {
          "mountPath": "/etc/tower/SECRET_KEY",
          "name": "awx-secret-key",
          "readOnly": true,
          "subPath": "SECRET_KEY"
        },
        {
          "mountPath": "/etc/tower/settings.py",
          "name": "awx-settings",
          "readOnly": true,
          "subPath": "settings.py"
        },
        {
          "mountPath": "/var/run/redis",
          "name": "awx-redis-socket"
        },
        {
          "mountPath": "/var/run/awx-rsyslog",
          "name": "rsyslog-socket"
        },
        {
          "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
          "name": "kube-api-access-j9sbr",
          "readOnly": true
        }
      ]
    }
  ],
  "dnsPolicy": "ClusterFirst",
  "enableServiceLinks": true,
  "nodeName": "minikube",
  "preemptionPolicy": "PreemptLowerPriority",
  "priority": 0,
  "restartPolicy": "Always",
  "schedulerName": "default-scheduler",
  "securityContext": {},
  "serviceAccount": "awx",
  "serviceAccountName": "awx",
  "terminationGracePeriodSeconds": 30,
  "tolerations": [
    {
      "effect": "NoExecute",
      "key": "node.kubernetes.io/not-ready",
      "operator": "Exists",
      "tolerationSeconds": 300
    },
    {
      "effect": "NoExecute",
      "key": "node.kubernetes.io/unreachable",
      "operator": "Exists",
      "tolerationSeconds": 300
    }
  ],
  "volumes": [
    {
      "name": "awx-receptor-ca",
      "secret": {
        "defaultMode": 420,
        "secretName": "awx-receptor-ca"
      }
    },
    {
      "name": "awx-receptor-work-signing",
      "secret": {
        "defaultMode": 420,
        "secretName": "awx-receptor-work-signing"
      }
    },
    {
      "name": "awx-application-credentials",
      "secret": {
        "defaultMode": 420,
        "items": [
          {
            "key": "credentials.py",
            "path": "credentials.py"
          },
          {
            "key": "ldap.py",
            "path": "ldap.py"
          },
          {
            "key": "execution_environments.py",
            "path": "execution_environments.py"
          }
        ],
        "secretName": "awx-app-credentials"
      }
    },
    {
      "name": "awx-secret-key",
      "secret": {
        "defaultMode": 420,
        "items": [
          {
            "key": "secret_key",
            "path": "SECRET_KEY"
          }
        ],
        "secretName": "awx-secret-key"
      }
    },
    {
      "configMap": {
        "defaultMode": 420,
        "items": [
          {
            "key": "settings",
            "path": "settings.py"
          }
        ],
        "name": "awx-awx-configmap"
      },
      "name": "awx-settings"
    },
    {
      "configMap": {
        "defaultMode": 420,
        "items": [
          {
            "key": "nginx_conf",
            "path": "nginx.conf"
          }
        ],
        "name": "awx-awx-configmap"
      },
      "name": "awx-nginx-conf"
    },
    {
      "configMap": {
        "defaultMode": 420,
        "items": [
          {
            "key": "redis_conf",
            "path": "redis.conf"
          }
        ],
        "name": "awx-awx-configmap"
      },
      "name": "awx-redis-config"
    },
    {
      "configMap": {
        "defaultMode": 420,
        "items": [
          {
            "key": "uwsgi_conf",
            "path": "uwsgi.conf"
          }
        ],
        "name": "awx-awx-configmap"
      },
      "name": "awx-uwsgi-config"
    },
    {
      "emptyDir": {},
      "name": "awx-redis-socket"
    },
    {
      "emptyDir": {},
      "name": "awx-redis-data"
    },
    {
      "emptyDir": {},
      "name": "rsyslog-socket"
    },
    {
      "emptyDir": {},
      "name": "receptor-socket"
    },
    {
      "configMap": {
        "defaultMode": 420,
        "items": [
          {
            "key": "receptor_conf",
            "path": "receptor.conf"
          }
        ],
        "name": "awx-awx-configmap"
      },
      "name": "awx-receptor-config"
    },
    {
      "name": "kube-api-access-j9sbr",
      "projected": {
        "defaultMode": 420,
        "sources": [
          {
            "serviceAccountToken": {
              "expirationSeconds": 3607,
              "path": "token"
            }
          },
          {
            "configMap": {
              "items": [
                {
                  "key": "ca.crt",
                  "path": "ca.crt"
                }
              ],
              "name": "kube-root-ca.crt"
            }
          },
          {
            "downwardAPI": {
              "items": [
                {
                  "fieldRef": {
                    "apiVersion": "v1",
                    "fieldPath": "metadata.namespace"
                  },
                  "path": "namespace"
                }
              ]
            }
          }
        ]
      }
    }
  ]
}
```
