module github.com/micro/micro/plugin/kafka/broker/v3

go 1.15

require (
	github.com/Shopify/sarama v1.19.0
	github.com/google/uuid v1.1.2
	github.com/micro/micro/v3 v3.3.0
)

replace github.com/micro/micro/v3 v3.3.0 => ../../..
