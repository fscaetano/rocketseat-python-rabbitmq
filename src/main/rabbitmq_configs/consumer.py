import pika
import json

def rabbitmq_callback(channel, method, properties, body):
    msg_bytes = body.decode("utf-8")
    msg = json.loads(msg_bytes)
    print(msg)
    print(type(msg))


class RabbitMQConsumer:
    def __init__(self) -> None:
        self.__host = "localhost"
        self.__port = 5672
        self.__username = "guest"
        self.__password = "guest"
        self.__queue = "my_queue"
        self.__routing_key = ""
        self.__channel = self.create_channel()

    def create_channel(self):
        connection_parameters = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            credentials=pika.PlainCredentials(
                username=self.__username, password=self.__password
            ),
        )
        channel = pika.BlockingConnection(connection_parameters).channel()
        channel.queue_declare(self.__queue, durable=True)
        channel.basic_consume(
            queue=self.__queue, auto_ack=True, on_message_callback=rabbitmq_callback
        )

        return channel

    def start(self):
        print("Connected to RabbitMQ")
        self.__channel.start_consuming()