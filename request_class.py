import requests
import os


class ImageJpeg:
    def __init__(self, image_url, image_list=[]):
        self.image_url = image_url
        self.image_list = image_list

    def __str__(self):
        return f"The url you requested is: {self.image_url}"

    def image_links_list(self, text_file):
        with open(text_file, "r") as file:
            for row in file:
                self.image_list.append(row)
        return self.image_list

    def download_jpg(self):
        resp = requests.get(self.image_url)
        if resp.status_code in (200, 400):
            name, extension = os.path.splitext(self.image_url)
            if extension == ".jpg":
                with open("jpg_image.jpg", "wb") as file:
                    file.write(resp.content)
            else:
                print(f"'{self.image_url}' not a jpeg file.")


class ImagePng(ImageJpeg):
    def __init__(self, image_url):
        super().__init__(image_url)

    def download_png(self):
        resp = requests.get(self.image_url)
        if resp.status_code in (200, 400):
            name, extension = os.path.splitext(self.image_url)
            if extension == ".png":
                with open("png_image.png", "wb") as file:
                    file.write(resp.content)
            else:
                print(f"'{self.image_url}' not a png file.")


image1 = ImagePng("https://upload.wikimedia.org/wikipedia/commons/2/27/Morskie_Oko_Poland_Winter.jpg")
image2 = ImagePng("https://imgs.xkcd.com/s/temperature.png")
print(image1.image_links_list("image_links"))
image2.download_png()



