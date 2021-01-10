import pika

def main():
    
    #Conexion Inicial
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    QUERY = 'Lucho Jara'

    #Creacion de Colas
    channel.queue_declare(queue='wikipedia')
    channel.queue_declare(queue='youtube')

    #Envio de QUERY
    print('  [*] Enviando "{}" a Wiki'.format(QUERY))
    channel.basic_publish(exchange='',
                        routing_key='wikipedia',
                        body=QUERY)

    print('  [*] Enviando "{}" a youtube'.format(QUERY))
    channel.basic_publish(exchange='',
                        routing_key='youtube',
                        body=QUERY)

if __name__ == "__main__":
    main()
