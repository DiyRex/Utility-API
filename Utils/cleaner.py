import os

path_list = ["Base64/decode","Base64/encode","Docs","download","QR","Local","QR_Gen","QR_ReGen","Text_to_voice"]
def cleaner():
    for path in path_list:
        files_list = os.listdir(path)
        for file in files_list:
            os.remove(os.path.join(path,file))
