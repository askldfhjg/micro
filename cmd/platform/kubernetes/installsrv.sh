cd #!/bin/bash

if [ $MICRO_ENV == "dev" ]; then
  sed -i '' 's/\*.m3o.app/\*.mcbeam.dev/g' 'ls ./service'
  sed -i '' 's/m3o.com/mcbeam.dev/g' ingress.yaml
fi

if [ $MICRO_ENV == "dev" ]; then
  sed -i '' 's/mcbeam-dev:mcbeam-dev-20210908-867303f91a12c8ead9509aaf90bd4cbbdc1b348c/mcbeam-dev:mcbeam-dev-20210908-efe81c2750022401b623ef6b32e892056353136b/g' `ls ./service/*`
  sed -i '' 's/- name: qcloudregistrykey//g'  `ls ./service/*`
kubectl apply -f service

win:
  sed -i '' 's/mcbeam.tencentcloudcr.com\/wolfplus\/mcbeam:mcbeam-0311/mcbeam-hub.tencentcloudcr.com\/wolfplus\/mcbeam-dev:mcbeam-dev-20210809-668f94da117f906a3259f671f815dce6e169602b/g' `ls ./service/*`
kubectl run cockroachdb --image=ubuntu -it --rm --restart=Never --overrides='
{
  "spec": {
    "template": {
      "spec": {
        "containers": [
          {
            "image": "ubuntu",
            "volumeMounts": [{
              "readOnly": true,
              "mountPath": "/certs/store",
              "name": "cockroachdb-client-certs"
            }]
          }
        ],
        "volumes": [{
          "name":"cockroachdb-client-certs",
          "secret": {
            "secretName": "cockroachdb-client-certs",
            "defaultMode": "0600"
          }
        }]
      }
    }
  }
}
' -- bash
