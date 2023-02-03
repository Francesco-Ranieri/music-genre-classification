import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from src.pathUtils import PathUtils


def plot_melspectrogram(song_name: str):
    y, sr = librosa.load(song_name, mono=True, duration=2, offset=2 * 2)
    ps = librosa.feature.melspectrogram(
        y=y, sr=sr, hop_length=256, n_fft=512, n_mels=64)
    ps = librosa.power_to_db(ps ** 2)

    stft = librosa.stft(y)
    s_db = librosa.amplitude_to_db(np.abs(stft), ref=np.max)

    plt.figure()
    librosa.display.specshow(s_db)
    plt.colorbar()
