import os

path = "/user/home/ishan/Desktop/logs"

for filename in os.listdir(path):
    filmame = os.path.join(folder, filename)

    if os.path.isfile(filepath):
        with open(filepath, "r") as f:
            for line in f:
                if "payment_failed" in line:
                    print(line)