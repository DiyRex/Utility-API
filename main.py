import os
import shutil
import qrcode
import random
import string
import uvicorn
import gunicorn
from PIL import Image
from typing import Optional
from pyzbar.pyzbar import decode
from fastapi.responses import FileResponse
from fastapi import FastAPI, UploadFile, File, Request
from Utils.pixcels import pixels
from Utils.cleaner import cleaner
from Utils.dotmail import dot_mail
from Utils.translate import translate
from Utils.doc_convert import convert
from Utils.fakebio import fake_profile
from Utils.string_gen import adv_password
from Utils.text_to_voice import Txt_voice
from Utils.image_search import search_images
from Utils.cc_gen import generate_cards, valid_cards
from Utils.base_64 import encode_base64, decode_base64

from Utils.dup import duplicate
from Utils.suffix import make_suffix
from Utils.prefix import make_prefix
from Utils.add_numberlines import number_lines

print("Server is running :)")
print(".....................")

APP_NAME = os.environ.get('APP_NAME')
host_url = "https://" + APP_NAME + ".herokuapp.com"

app = FastAPI(docs_url=None)

@app.get("/")
async def root():
    return {"Server_Stats": "Online","Usage":{"Generate QR image from text":f"{host_url}/qr_gen?text=[text]",
    "Generate QR String form QR Image":f"{host_url}/qr[post_image]",
    "Recreate QR image from captured Image":f"{host_url}/re_qr[post_image]",
    "Encode image and get base64 data":f"{host_url}/img_encode[post_image]",
    "Convert PPTX to PDF":f"{host_url}/pptopdf[post_file]",
    "Add suffix to lines in txt file":f"{host_url}/suffix[post_file]",
    "Add prefix to lines in txt file":f"{host_url}/prefix[post_file]",
    "Add number to lines in txt file":f"{host_url}/addnum[post_file]",
    "Remove duplicate lines in txt file":f"{host_url}/remdup[post_file]",
    "Search images and receive as zip":f"{host_url}/img_search?keyword=[keyword]&count=[count]",
    "Generate cc from bin":f"{host_url}/cc_gen?bin=[bin]?year=[year]&month=[month]&ccv=[ccv]&amount=[amount]",
    "Generate List of passwords":f"{host_url}/pwd_gen?length=[length]&amount=[amount]",
    "Generate fake profile":f"{host_url}/fake",
    "Generate dot mails from gmail":f"{host_url}/dotmail?email=[email]",
    "Generate voice from text":f"{host_url}/txt_voice?text=[text]",
    "Translate text (Google Translate)":f"{host_url}/translate?text=[text]&language=[language]",
    "Get Images from Pixels":f"{host_url}/pixels?keyword=[keyword]&page=[pageNo]&count=[count]",
    },
    "Owned by":"DiyRex from D-soft Labs"
}


@app.get("/qr_gen")
async def QR_Image_Generate(text: Optional[str] = None):
    cleaner()
    name = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(8))
    img = qrcode.make(text)
    file_name = f'QR_Gen/qrcode_{name}.png'
    img.save(file_name)
    cleaner(file_path=file_name)
    return FileResponse(file_name,filename=f"qrcode_{name}.png")



@app.post("/qr")
async def QR_to_String(file: UploadFile = File(...)):
    with open("QR/"+file.filename, "wb") as buffer :
        shutil.copyfileobj(file.file,buffer)
        data = decode(Image.open(file.filename))
        string_qr = data[0][0]
    os.remove("QR/"+file.filename)
    return {"data": string_qr}

@app.post("/re_qr")
async def Recreate_QR(file: UploadFile = File(...)):
    cleaner()
    with open("QR_ReGen/"+file.filename, "wb") as buffer :
        shutil.copyfileobj(file.file,buffer)
        data = decode(Image.open(file.filename))
        string_qr = data[0][0]
        name = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(8))
        img = qrcode.make(string_qr)
        file_name = f'QR_ReGen/qrcode_{name}.png'
        img.save(file_name)
    return FileResponse(file_name,filename=f"qrcode_{name}.png")

@app.post("/pptopdf")
async def PPTX_to_PDF_Convert(file: UploadFile = File(...)):
    cleaner()
    with open("Docs/"+file.filename, "wb") as buffer :
        shutil.copyfileobj(file.file,buffer)
        data = convert(file.filename)
        name = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(4))
    try:
        return FileResponse(data,filename=f"ppdf_{name}.pdf")
    except: return data

@app.post("/suffix")
async def Add_Suffix(file: UploadFile = File(...),suffix: Optional[str] = None):
    cleaner()
    with open("Docs/"+file.filename, "wb") as buffer :
        shutil.copyfileobj(file.file,buffer)
        file = make_suffix(file_path=file.filename,suffix=suffix)
    return FileResponse(file,filename="suffiex.txt")

@app.post("/prefix")
async def Add_Prefix(file: UploadFile = File(...),prefix: Optional[str] = None):
    cleaner()
    with open("Docs/"+file.filename, "wb") as buffer :
        shutil.copyfileobj(file.file,buffer)
        file = make_prefix(file_path=file.filename,prefix=prefix)
    return FileResponse(file,filename="prefix.txt")

@app.post("/addnum")
async def Add_Number_lines(file: UploadFile = File(...)):
    cleaner()
    with open("Docs/"+file.filename, "wb") as buffer :
        shutil.copyfileobj(file.file,buffer)
        file = number_lines(file_path=file.filename)
    return FileResponse(file,filename="numberd.txt")

@app.post("/remdup")
async def Remove_Duplicate_lines(file: UploadFile = File(...)):
    cleaner()
    with open("Docs/"+file.filename, "wb") as buffer :
        shutil.copyfileobj(file.file,buffer)
        file = duplicate(file_path=file.filename)
    return FileResponse(file,filename="dup_cleaned.txt")

@app.get("/img_search")
async def Image_Search(keyword: Optional[str] = None,count: Optional[int] = None):
    cleaner()
    image_zip = search_images(keyword=keyword,count=count,path="download")
    return FileResponse(image_zip[0],filename=image_zip[1])
    #return {"zip_path":image_zip}

@app.get("/cc_gen")
async def Card_Generate(bin: Optional[str] = None, year: Optional[str] = None, month: Optional[str] = None, ccv: Optional[str] = None, amount: Optional[int] = None):
    cards = valid_cards(bin=bin, year=year, month=month, ccv=ccv,amount=amount)
    return {"Cards":cards}

@app.post("/img_encode")
async def image_encode(file: UploadFile = File(...)):
    cleaner()
    with open("Base64/encode/"+file.filename, "wb") as buffer :
        shutil.copyfileobj(file.file,buffer)
        data = encode_base64(file.filename)
    os.remove("Base64/encode/"+file.filename)
    return {"data": data}

@app.get("/img_decode")
async def image_decode(encoded_data: Optional[str] = None):
    cleaner()
    img_path = decode_base64(encoded_data)
    return FileResponse(img_path,filename="encoded_image.png")

@app.get("/pwd_gen")
async def Password_Generate(length: Optional[int] = None, amount: Optional[int] = None):
    pwd = adv_password(amount=amount,length=length)
    return {"Passwords":pwd}

@app.get("/fakedata")
async def Fake_Profile_Generate():
    profile = fake_profile()
    return {"Profile":profile}

@app.get("/dotmail")
async def Dot_Mail_Generate(email: Optional[str] = None):
    mails = dot_mail(email)
    return {"dot_mails":mails}

@app.get("/txt_voice")
async def Text_to_voice(text: Optional[str] = None):
    cleaner()
    file = Txt_voice(text)
    return FileResponse(file,filename="voice.mp3")

@app.get("/translate")
async def Google_Translate(text: Optional[str] = None,lan: Optional[str] = None):
    tran_text = translate(text=text,language=lan)
    return {"Translated Text":tran_text}

@app.get("/pixels")
async def Pixels_Image_Search(keyword: Optional[str] = None,page: Optional[int] = None,result: Optional[int] = None):
    pixels_urls = pixels(keyword=keyword,page=page,result=result)
    return {"Images":pixels_urls}

