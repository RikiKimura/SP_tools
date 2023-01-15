import sounddevice as sd
import soundfile as sf
from scipy.io import wavfile


print(sd.query_devices()) # デバイス番号確認

sd.default.device = [1,2] # 入出力デバイス番号[in,out]
sd.default.channels = 1


input_filename = "play.wav"
output_filename = "rec.wav"

wav, fs = sf.read(input_filename)

record = sd.playrec(wav, fs, dtype='int16')
sd.wait()

wavfile.write(output_filename, fs, record)