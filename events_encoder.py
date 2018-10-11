import logging, datetime, time
from kafka_influxdb.encoder.escape_functions import influxdb_tag_escaper

try:
    # Test for mypy support (requires Python 3)
    from typing import Text
except ImportError:
    pass


data_fieldnames = [ "published", "processed", "published_predict_prob", "processed_predict_prob", "isAnomly" ]

class Encoder(object):
    """
    Encoder for Events data formatted as this per line:
    "published", "processed", "published_predict_prob", "processed_predict_prob", "isAnomly" 
    """

    def __init__(self):
        self.escape_tag = influxdb_tag_escaper()

    def encode(self,
               msg):
        # type: (bytes, Text, Text, Text, Text, Text) -> List[Text]
        """
        :param msg: Payload from reader
        :return: A list of encoded messages
        """
        # One message could consist of several measurements
        # print msg, "->"
        measurements = []

        for i, val in enumerate(msg.split(",")):
            encoded = ''.join([
                str(data_fieldnames[i]),
                # ",",
                ' value=',
                str(val),
                ' ',
                str(int(time.time()))
                ])
            measurements.append(encoded)

        return measurements
