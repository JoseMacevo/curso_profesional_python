import time
import logging
import threading

logging.basicConfig(level=logging.DEBUG,
                    format='%(message)s')


def thread():
    logging.info("Hi, I'm a normal thread...")
    time.sleep(2)
    logging.info("The program ends when I end....")


def daemon_thread():
    while True:
        logging.info("We are executing in the background..")
        time.sleep(0.5)


if __name__ == '__main__':
    thread_1 = threading.Thread(target=daemon_thread, daemon=True)
    thread_1.start()
    input("Press a key to ending the mainthread")
