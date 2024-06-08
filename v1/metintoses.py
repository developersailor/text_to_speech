from gtts import gTTS

# Metni ve dili belirleyin
metin = "Merhaba, ben Bard! Metni sese dönüştürmek için Python'u nasıl kullanacağınızı öğreniyorsunuz."
dil = 'tr'

# Seslendirmeyi oluşturun
ses = gTTS(text=metin, lang=dil)

# Ses dosyası olarak kaydedin
ses.save("sesli_metin.mp3")