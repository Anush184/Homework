import logging
import time
import datetime
import random
import concurrent.futures
import threading


def logging_number(num):
    logging.basicConfig(filename='example.log', filemode='a', datefmt='%m-%d-%y %I:%M',
                        format='%(asctime)s %(levelname)s: %(message)s', level=logging.DEBUG)
    if num in range(0, 10):
        logging.debug(F"The temperature is {num} degree. Recommended to dress warmly")
    elif num in range(10, 20):
        logging.info(F"The temperature is {num} degree. It is sunny, no rain is expected")
    elif num in range(20, 30):
        logging.warning(F"The temperature is {num} degree. It is hot weather, "
                        F"beware of direct sunlight")
    elif num in range(30, 40):
        logging.error(F"The temperature is {num} degree. Don't stay outside for long.")
    else:
        logging.critical(F"The temperature is {num} degree. It is strictly forbidden to go out.")


if __name__ == "__main__":
    #version 1
    # with concurrent.futures.ThreadPoolExecutor() as executor:
    # executor.map(logging_number, num_list)
    #version2
    num_list = []
    for i in range(10):
        number = random.randint(0, 50)
        num_list.append(number)

    start = datetime.datetime.today()
    print(start)
    thread_list = []
    for _ in range(10):
        x = threading.Thread(target=logging_number, args=(random.randint(0, 50), ), daemon=True)
        thread_list.append(x)
        x.start()
        #time.sleep(0.5)
    for thread in thread_list:
        thread.join()

    finish = datetime.datetime.today()
    print(f"Finished in {(finish - start).seconds} second's ")
