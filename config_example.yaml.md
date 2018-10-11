---
kafka:
  host: "localhost"
  port: 9092
  topic: "salesforce-stream-in"
  group: "kafka-influxdb"
  reader: "kafka_influxdb.reader.confluent"
  #reader: "kafka_influxdb.reader.kafka_python" # Legacy consumer
influxdb:  
  host: "localhost"
  port: 8086
  user: "admin"
  password: "admin"
  dbname: "influx"
  use_ssl: false
  verify_ssl: False
  timeout: 5
  use_udp: False
  retention_policy: "autogen"
  time_precision: "s"
encoder: "kafka_influxdb.encoder.events_encoder"
buffer_size: 1000
statistics: true