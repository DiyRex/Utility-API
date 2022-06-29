from gtts import gTTS
import os
  

def Txt_voice(text):
    language = 'en'
    myobj = gTTS(text=text, lang=language, slow=False)
    myobj.save("Text_to_Voice/voice.mp3")
    return "Text_to_Voice/voice.mp3"
