import pika
import youtubesearchpython

def main():
    #Conexión al servidor RabbitMQ   
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='youtube')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body.decode())

        #Busqueda en Youtube
        busqueda = youtubesearchpython.VideosSearch(body.decode(), limit = 1).result()
        print("Nombre Video: {}\nDuracion Video: {}\nVisitas: {}\nLink: {}".format(busqueda["result"][0]["title"], busqueda["result"][0]["duration"], busqueda["result"][0]["viewCount"]["short"],busqueda["result"][0]["link"]))

	

    channel.basic_consume(queue='youtube', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    

if __name__ == "__main__":
    main()
