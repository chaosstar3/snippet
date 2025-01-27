> bin/kafka-console-producer.sh --bootstrap-server {server} --topic {topic}
> bin/kafka-console-consumer.sh --bootstrap-server {server} --from-beginning --group {group} --topic {topic}
## add
### kafka-connector

es_sink
```properties
name=es-sink
connector.class=io.confluent.connect.elasticsearch.ElasticsearchSinkConnector

tasks.max=1
topics={topic}

connection.url={es_url}
connection.username={username}
connection.password={password}

type.name=_doc

value.converter=org.apache.kafka.connect.json.JsonConverter
value.converter.schema.enable=false
schema.ignore=true
key.ignore=true
```
connect-properties
> plugin.path=plugins/confluentinc-kafka-connect-elasticsearch-11.2.8

run
> bin/connect-standalone.sh connect-standalone.properties es_sink.properties

### kafka-ui

> docker run -it --name kafka-ui -p {port}:8080 -e DYNAMIC_CONFIG_ENABLE=true provectuslabs/kafka-ui
