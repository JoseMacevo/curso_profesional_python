import logging
import requests
import threading

logging.basicConfig(level=logging.DEBUG,
                    format='%(message)s')


def get_pokemon_name():
    pass


def error():
    pass


def generate_request(url, success_callback, error_callback):
    response = requests.get(url)
    if response.status_code == 200:
        success_callback()
    else:
        error_callback()


if __name__ == "__main__":
    thread_1 = threading.Thread(target=generate_request, kwargs={
        "url": "https://pokeapi.co/api/v2/pokemon/1/",
        "success_callback": get_pokemon_name,
        "error_callback": error
    })
    thread_1.start()

# Seguir desde aqui....05:04 min