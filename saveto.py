import sys
import speech_recognition as sr
from pydub import AudioSegment
from gtts import gTTS
from PyQt5 import QtWidgets

class VoiceProcessorApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Voice Processor')
        self.setGeometry(100, 100, 400, 200)

        self.recordButton = QtWidgets.QPushButton('Ses Kaydet', self)
        self.recordButton.setGeometry(50, 50, 100, 50)
        self.recordButton.clicked.connect(self.record_voice)

        self.statusLabel = QtWidgets.QLabel('Durum: Hazır', self)
        self.statusLabel.setGeometry(50, 120, 300, 50)
        
    def record_voice(self):
        self.statusLabel.setText("Durum: Kaydediliyor...")
        QtWidgets.QApplication.processEvents()
        
        recognizer = sr.Recognizer()
        mic = sr.Microphone()

        with mic as source:
            print("Konuşmaya başla  yın...")
            audio = recognizer.record(source, duration=5)
            print("Kayıt tamamlandı.")

        try:
            text = recognizer.recognize_google(audio, language="tr-TR")
            print("Tanınan metin:", text)
            self.statusLabel.setText(f"Tanınan metin: {text}")
        except sr.UnknownValueError:
            print("Ses tanınamadı.")
            self.statusLabel.setText("Ses tanınamadı.")
        except sr.RequestError as e:
            print("Google API hatası:", e)
            self.statusLabel.setText(f"Google API hatası: {e}")
        
        self.process_voice(text)
    
    def process_voice(self, text):
        voice_data = AudioSegment.from_file("input.wav")
        voice_data = voice_data.set_frame_rate(16000)
        
        tts = gTTS(text=text, lang="tr")
        tts.save("metinden_sese.mp3")
        
        combined_audio = voice_data + AudioSegment.from_file("metinden_sese.mp3")
        combined_audio.export("sonuc.wav")
        
        self.statusLabel.setText("Sonuç ses dosyası oluşturuldu: sonuc.wav")
        print("Sonuç ses dosyası oluşturuldu: sonuc.wav")
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = VoiceProcessorApp()
    ex.show()
    sys.exit(app.exec_())