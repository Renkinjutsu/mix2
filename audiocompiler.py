import numpy as np
import audiofile as af
import soundfile as sf
from playsound import playsound
from AppKit import NSSound
from Foundation import NSURL
import librosa


sig, fs = af.read('pianotest.mp3')

file_path = "pianotest.mp3"
samples, sampling_rate = librosa.load(file_path, sr =None, mono = True, offset = 0.0, duration = None)
sample2, sampling_rate2 = librosa.load("test2.aiff", sr =None, mono = True, offset = 0.0, duration = None)


if samples.size  > sample2.size:
  appendNum = samples.size - sample2.size
  newArray = np.repeat(0, appendNum)
  print("newArray", newArray)
  sample2 = np.append(sample2, newArray)
  print("sample2", sample2)
elif samples.size < sample2.size:
  appendNum = sample2.size - samples.size
  newArray = np.repeat(0, appendNum)
  print("newArray", newArray)
  samples = np.append(samples, newArray)
  print("sample", samples)

print("new length", samples.size, sample2.size)
if samples.size == sample2.size:
  print("go time")

  tmpArr = [
    (samples[x] + sample2[x]) / 2
    for x in range(round(samples.size))
  ]

  newSoundArr = np.array(tmpArr)

  print("NEW SOUND ARR", newSoundArr.size)

  sf.write("newSound.wav", newSoundArr, sampling_rate, subtype='PCM_24')
  print("it is written")

print("it is playing")
playsound("newSound.wav")


# 1. find reliable compression and expansion - regulate sampling rate
# 2. merge 2 clips of different lengths will merge together (tacking on no sound at the end to the clips are equal). maybe loop at end?
# 3. autotuning - python modules for autotuning. consider only allowing for 1 autotuning setting
# 4. XXX @Dru take a look at this: https://github.com/jiaaro/pydub/blob/master/API.markdown
# 5. play as it's compiling instead of compiling to new file? further investigation (punt it to future because chunking mp3 files is a big lift)
# 6. regulate volume? 