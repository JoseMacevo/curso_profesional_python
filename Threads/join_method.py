import time
import logging
import threading

logging.basicConfig(level=logging.DEBUG,
                    format='%(message)s')


def data_base_connection():
    logging.info('Starting conexion with de dabase')
    time.sleep(2)


def web_server_query():
    logging.info("Starting web server query...")
    time.sleep(2.5)


if __name__ == '__main__':
    thread_1 = threading.Thread(target=data_base_connection)
    thread_2 = threading.Thread(target=web_server_query)
    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()


    logging.info("Ending programm, the threads has ending...")


