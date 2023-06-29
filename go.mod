module github.com/micro/micro/v3

go 1.15

require (
	github.com/HdrHistogram/hdrhistogram-go v1.1.0 // indirect
	github.com/bitly/go-simplejson v0.5.0
	github.com/caddyserver/certmagic v0.10.6
	github.com/chzyer/readline v0.0.0-20180603132655-2972be24d48e
	github.com/davecgh/go-spew v1.1.1
	github.com/dgrijalva/jwt-go v3.2.0+incompatible
	github.com/dustin/go-humanize v1.0.0
	github.com/evanphx/json-patch/v5 v5.0.0
	github.com/getkin/kin-openapi v0.26.0
	github.com/go-acme/lego/v3 v3.4.0
	github.com/gofrs/uuid v3.2.0+incompatible
	github.com/golang/protobuf v1.4.3
	github.com/google/uuid v1.1.2
	github.com/gorilla/handlers v1.4.2
	github.com/gorilla/mux v1.7.3
	github.com/gorilla/websocket v1.4.2
	github.com/hashicorp/go-version v1.2.1
	github.com/hpcloud/tail v1.0.0
	github.com/improbable-eng/grpc-web v0.13.0
	github.com/kr/pretty v0.2.0
	github.com/micro/micro/plugin/etcd/v3 v3.0.0-20210901132929-6f7737ba4064
	github.com/micro/micro/plugin/kafka/broker/v3 v3.0.0-00010101000000-000000000000
	github.com/micro/micro/plugin/prometheus/v3 v3.0.0-20210825142032-d27318700a59
	github.com/miekg/dns v1.1.27
	github.com/nightlyone/lockfile v1.0.0
	github.com/olekukonko/tablewriter v0.0.4
	github.com/onsi/gomega v1.10.5
	github.com/opentracing/opentracing-go v1.2.0
	github.com/oxtoacart/bpool v0.0.0-20190530202638-03653db5a59c
	github.com/patrickmn/go-cache v2.1.0+incompatible
	github.com/philchia/agollo/v4 v4.1.3
	github.com/pkg/errors v0.9.1
	github.com/schollz/progressbar/v3 v3.8.2
	github.com/serenize/snaker v0.0.0-20171204205717-a683aaf2d516
	github.com/stoewer/go-strcase v1.2.0
	github.com/stretchr/objx v0.1.1
	github.com/stretchr/testify v1.7.0
	github.com/teris-io/shortid v0.0.0-20171029131806-771a37caa5cf
	github.com/uber/jaeger-client-go v2.29.1+incompatible
	github.com/uber/jaeger-lib v2.4.1+incompatible // indirect
	github.com/urfave/cli/v2 v2.3.0
	github.com/wolfplus2048/mcbeam-plugins/config/apollo/v3 v3.0.0-20210826053511-6966876170a7
	github.com/wolfplus2048/mcbeam-plugins/session/v3 v3.0.0-20210803053144-09b3e552dd3e
	github.com/wolfplus2048/mcbeam-plugins/ws_session/v3 v3.0.0-20211015055059-04d181a0021c
	github.com/xanzy/go-gitlab v0.35.1
	github.com/xlab/treeprint v0.0.0-20181112141820-a009c3971eca
	go.etcd.io/bbolt v1.3.5
	golang.org/x/crypto v0.0.0-20210616213533-5ff15b29337e
	golang.org/x/net v0.0.0-20210226172049-e18ecbb05110
	google.golang.org/genproto v0.0.0-20200526211855-cb27e3aa2013
	google.golang.org/grpc v1.27.0
	google.golang.org/protobuf v1.26.0-rc.1
)

replace (
	github.com/micro/micro/plugin/etcd/v3 => ./plugin/etcd
	github.com/micro/micro/plugin/kafka/broker/v3 => ./plugin/kafka/broker
	github.com/micro/micro/plugin/prometheus/v3 => ./plugin/prometheus
	google.golang.org/grpc => google.golang.org/grpc v1.27.0
)
