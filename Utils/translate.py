from googletrans import Translator

def translate(text,language):
    translator = Translator()

    # translated_text = translator.translate('안녕하세요.')
    # print(translated_text.text)

    translated_text = translator.translate(text, dest=language)
    # print(translated_text.text)

    # translated_text = translator.translate('veritas lux mea', src='la')
    # print(translated_text.text)
    return translated_text.text