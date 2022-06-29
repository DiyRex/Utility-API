from icrawler.builtin import GoogleImageCrawler
from zipfile import ZipFile, ZIP_DEFLATED
import os
import random
import string

def search_images(keyword,count,path):
    google_crawler = GoogleImageCrawler(storage={'root_dir': 'downloads'})
    google_crawler.crawl(keyword=keyword, max_num=count)

    file_name = "image_result_"+''.join(random.choice(string.ascii_lowercase+string.ascii_uppercase+string.digits)for p in range(5))
    print(f"filename is {file_name}")
    zip_o = os.path.join(path,file_name+".zip")
    zipObj = ZipFile(zip_o, 'w')

    for i in os.listdir(path):
        ext = os.path.splitext(i)[-1].lower()
        if ext == ".jpg" or ext == ".png" or ext == ".jpeg":
            print(i)
            zipObj.write(os.path.join(path,i),i)
            os.remove(os.path.join(path,i))
        else:
            pass
    return zip_o, file_name+".zip"

# print(search_images(keyword="apple",count=10))