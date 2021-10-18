import json
import os
import requests
import threading


def download():
    with open('zjl.json', encoding='utf-8') as f:
        content = json.load(f)
        f.close()
        for k in content:
            # print(k["wma"])
            # print(k["mname"])
            if k["wma"] != "0":
                threading.Thread(target=down_load,
                                 args=([k["wma"], "D:/opsProject/svn/trunk/cgameai/mp3", k["mname"]])).start()


# 文件下载器
def down_load(file_url, file_path, file):
    print(file_url + " ---------" + file)
    r = requests.get(file_url)
    if not os.path.exists(file_path):
        os.makedirs(file_path)
        with open(file_path + "/" + file + ".mp3", "wb") as f:  # wb：以二进制方式写入文件
            f.write(r.content)  # r.content：以二进制方式读取文件
    else:
        with open(file_path + "/" + file + ".mp3", "wb") as f:  # wb：以二进制方式写入文件
            f.write(r.content)  # r.content：以二进制方式读取文件


download()


