import os
from os import rename
import uuid

uuidCache = ["input,output"]
logStream = []

def prompt_input():
    inp = input("Path: ")
    if inp is None:
        return prompt_input()
    return inp

def is_valid_path(path):
    return os.path.exists(path)

def gen_uid():
    uid = uuid.uuid4()
    if uid in uuidCache:
        logStream.append(f"Duplicate UUID, generating new one.\n{uid}")
        print(f"Duplicate UUID, generating new one.\n{uid}")
        return gen_uid()
    else:
        uuidCache.append(uid)
        return uid

path = prompt_input()

if not is_valid_path(path):
    print("Path does not exist.")
    exit(1)

gen_log = input("Generate log file? (y/N): ")
gen_log_bool = False

if gen_log is None or gen_log == "n" or gen_log == "N":
    gen_log_bool = False
elif gen_log == "y" or gen_log == "Y":
    gen_log_bool = True

for file in os.listdir(path):
    fileending = file.split(".")[file.split(".").__len__() - 1]
    uid = gen_uid()
    try:
        rename(os.path.join(path, file), os.path.join(path, f"{uid}.{fileending}"))
        logStream.append(f"{file},{uid}.{fileending}")
        print(f"{uid}.{fileending}")
    except Exception as e:
        logStream.append(f"Error renaming {file} to {uid}.{fileending}")
        print(e)
        continue

if gen_log_bool:
    with open("log.txt", "w") as f:
        for line in logStream:
            f.write(f"{line}\n")
    print("Log file generated.")