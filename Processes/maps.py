import time
import logging
from multiprocessing import Pool

logging.basicConfig(level=logging.DEBUG,
                    format='%(processName)s %(message)s')

def is_even(number):
    time.sleep(1)
    return number % 2 == 0


def show_results(results):
    logging.info(f"The result is: {results}")


if __name__ == '__main__':
    with Pool(processes=2) as executor:
        numbers = [number for number in range(1, 10)]
        map_result = executor.map_async(is_even, numbers, callback=show_results)
        logging.info("We're waiting until the results are ready..")

        map_result.wait(timeout=1)
        logging.info(f"The result is: {map_result.get()}")

# Reproducir video desde el principio





