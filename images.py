#Download pictures
import json
import requests
import os
import time
import concurrent.futures


def download_image(image_url):
    response = requests.get(image_url)
    if response.status_code in (200, 400):
        name, extension = os.path.splitext(image_url)
        image_name = name.split("/")[-1]
        if extension == ".jpg":
            with open(f"{image_name}.png", "wb") as image_file:
                image_file.write(response.content)
                print(f"{image_name} was downloaded!")
        elif extension == ".png":
            with open(f"{image_name}.png", "wb") as image_file:
                image_file.write(response.content)
                print(f"{image_name} was downloaded!")
        else:
            raise IOError(f"Problem with '{image_name}'.")


if __name__ == "__main__":
    with open("fruits.json") as f:
        data = json.load(f)
    image_url_list = []
    for i in range(10):
        image_url_list.append(data["Fruits"][i]["photo"])

    start = time.perf_counter()
    print(start)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_image, image_url_list)

    finish = time.perf_counter()
    print(F"finished in {round(finish - start, 2)} second's")




