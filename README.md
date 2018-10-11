# Instructions (Kafka Consume pushing events data to grafana)

Steps to get kafka consumer running and pushing data to influx db with a grafana dashboard:

1) Clone the repo: https://github.com/BushnevYuri/DockerGrafanaInfluxKit

	Make sure you have docker-compose, then from inside the above repo folder run: 

			docker-compose up

	Login to the grafana container UI on localhost:3000 using the credentials in configuration.env file.

	Import the grafana dashboard using import via JSON file feature. Use the Grafana_Dashboard_AD.json file.

2) Clone this repo https://github.com/mre/kafka-influxdb

	Make the following changes:

	- Update the config_example.yaml as follows

	- Add the events_encoder.py as follows in the kafka_influxdb\encoder folder


3) From the cloned repo folder (kafka-influxdb), following command will run the consumer:

	kafka_influxdb -c config_example.yaml

4) Run the kafka console producer using a csv file with 5 columns of data as shown below:

	5.5,6.6,0.43,0.54,1

	2.0,2.5,0.33,0.44,0

	3.5,4.6,0.13,0.24,0

	10.5,11.6,0.23,0.44,0

	15.5,16.6,0.43,0.64,1


You should now be able to see data in the grafana dashboard charts.