import datetime
import time
import threading
from boto.kinesis.exceptions import ResourceNotFoundException
import boto
import boto3


#kinesis = boto.kinesis.connect_to_region("us-east-1")
kinesis=boto3.client('kinesis')

class KinesisProducer(threading.Thread):
    """Producer class for AWS Kinesis streams """

    def __init__(self, stream_name, sleep_interval=None, id='0'):
        self.stream_name = stream_name                  # name of stream in AWS
        self.sleep_interval = sleep_interval            # period of sending data
        self.id = id                                    # id of producer
        super().__init__()

    def put_record(self):
        """put a single record to the stream"""
        timestamp = datetime.datetime.utcnow()          # get date
        part_key = self.id                              # create key with id
        data = timestamp.isoformat()                    # convert date into useful format

        print(data)
        print(kinesis.put_record(StreamName=self.stream_name, Data=data, PartitionKey="1"))
        data = b"sasdsa" 
        print(data)
        print(kinesis.put_record(StreamName=self.stream_name, 
                                Data=data, 
                                PartitionKey="2sfsdfdsdsaf"))  # this should be veeeery different from "1" and "2"...

    def run_continously(self):
        """put a record at regular intervals"""
        while True:
            self.put_record()
            time.sleep(self.sleep_interval)

    def run(self):
        """run the producer"""
        try:
            if self.sleep_interval:
                self.run_continously()
            else:
                self.put_record()
        except ResourceNotFoundException:
            print('stream {} not found. Exiting'.format(self.stream_name))
            
            

stream_name = "poglad"

producer1 = KinesisProducer(stream_name, sleep_interval=2, id='2')
producer2 = KinesisProducer(stream_name, sleep_interval=5, id='1')
producer1.run_continously()
producer2.run_continously()