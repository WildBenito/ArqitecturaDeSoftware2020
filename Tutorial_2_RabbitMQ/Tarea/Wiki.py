import pika
import wikipedia

wikipedia.set_lang("es")
def main():
    #Aqui se conecta con RabbitMQ 
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='wikipedia')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body.decode())

        wikiquery = wikipedia.summary(body.decode(), sentences=3)

        print("\n{}\n".format(wikiquery))

    channel.basic_consume(queue='wikipedia', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    main()
