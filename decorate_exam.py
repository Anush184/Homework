import time
import datetime
import os


num = 0


def data_storage_file(filepath):
    def working_time(func):
        def inner(*args, **kwargs):
            global num
            num += 1
            comment = f"<{func.__name__}> function starts working!"
            print(comment)
            start_time = datetime.datetime.today()
            print("Start time:", start_time)
            result = func(*args, **kwargs)
            finish = datetime.datetime.today()
            print("End_time:", finish)
            end_time = (finish - start_time).seconds
            comment2 = f"<{func.__name__}> function finished working in {end_time} second's!"
            print(comment2)
            with open(filepath, "a", encoding="utf-8") as file:
                file.write(str(num) + ". " + comment + "\n")
                file.write(f"Start time: {start_time}\n")
                file.write(f"<{func.__name__}> function returns: {result}\n")
                file.write(f"End_time: {finish}\n")
                file.write(comment2 + "\n\n")
            return f"<{func.__name__}> function returns: {result}"
        return inner
    return working_time


data_file = os.path.join(os.getcwd(), "data_file.text")
count = 0


@data_storage_file(data_file)
def sum_of_numbers(a, b, c):
    time.sleep(2)
    return a + b + c


@data_storage_file(data_file)
def create_dict(**kwargs):
    dic = {}
    for key, value in kwargs.items():
        dic[key] = value
    print("Created dictionary:", dic)


print(sum_of_numbers(3, 4, 2))
print(create_dict(x=6, y=8, z=54, k="Hope"))
