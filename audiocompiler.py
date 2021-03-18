import numpy as np
import audiofile as af
import soundfile as sf
from playsound import playsound
from AppKit import NSSound
from Foundation import NSURL
import librosa


sig, fs = af.read('pianotest.mp3')
# print(f'sampling rate: {fs}, signal shape: {sig.size}')
# sound = NSSound.alloc()
# url = NSURL.URLWithString_('file://pianotest.mp3')
# sound.initWithContentsOfURL_byReference_(url, True)
# print("sound", sound.volume, sound.duration)
# sound.play()
# playsound('pianotest.mp3')
# playsound('test2.aiff')

file_path = "pianotest.mp3"
samples, sampling_rate = librosa.load(file_path, sr =None, mono = True, offset = 0.0, duration = None)
sample2, sampling_rate2 = librosa.load("test2.aiff", sr =None, mono = True, offset = 0.0, duration = None)
# y, sr = librosa.load('pianotest.mp3')

# S = np.abs(librosa.stft(samples))
print("123",len(samples), sampling_rate, "t2", sample2.size, sampling_rate2)


if samples.size  > sample2.size:
  appendNum = samples.size - sample2.size
  newArray = np.repeat(0, appendNum)
  print("newArray", newArray)
  sample2 = np.append(sample2, newArray)
  # for x in range(appendNum):
  #   sample2.append(0)
  print("sample2", sample2)
elif samples.size < sample2.size:
  appendNum = sample2.size - samples.size
  newArray = np.repeat(0, appendNum)
  print("newArray", newArray)
  samples = np.append(samples, newArray)
  # for x in range(appendNum):
  #   samples.append(0)
  print("sample", samples)

print("new length", samples.size, sample2.size)
if samples.size == sample2.size:
  print("go time")
  tmpArr= []
  for x in range(round(samples.size)):
    newValue = (samples[x] + sample2[x]) / 2
    tmpArr.append(newValue)

  print("tmp", len(tmpArr))
  newSoundArr = np.array(tmpArr)

  print("NEW SOUND ARR", newSoundArr.size)

  print("something")
  sf.write("newSound.wav", newSoundArr, sampling_rate, subtype='PCM_24')
  print("it is written")

print("it is playing")
playsound("newSound.wav")

print("something2")

# print("s", S) 
# librosa.display.waveplot(samples)
# len(samples), sampling_rate
