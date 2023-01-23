import math
import os

import librosa
import numpy as np
import pandas as pd
from scipy.io.wavfile import write


class FeatureExtractor:
    num_segment = 10
    duration = 66149
    sample_rate = 22050
    track_duration = 30
    hop_length = 512
    path_file = 'temp.wav'

    def __init__(self):
        self.sample_per_track = self.sample_rate * self.track_duration
        self.samples_per_segment = int(self.sample_per_track / 10)

    def _save_file(self, audio_array: np.array):
        """
        :param audio_array:
        :return:
        """

        scaled = np.int16(audio_array / np.max(np.abs(audio_array)) * 32767)
        write(self.path_file, self.sample_rate, scaled)

    def extract_feature(self, audio_array, num_segment: int = 10):
        """
        :param audio_array:
        :param num_segment:
        :return:
        """

        self._save_file(audio_array)
        signal, _ = librosa.load(self.path_file, sr=self.sample_rate)
        os.remove(self.path_file)

        gtzan_features = []
        mfcc_features = []

        for segment in range(num_segment):
            start = self.samples_per_segment * segment
            finish = start + self.samples_per_segment
            signal_split = signal[start:finish]
            gtzan_features.append(
                self._extract_gtzan_feature_from_segment(signal_split))
            mfcc_features.append(
                self._extract_and_format_mfcc_feature_from_segment(signal_split))

        return pd.DataFrame(data=gtzan_features), np.array(mfcc_features)[..., np.newaxis]

    def _extract_gtzan_feature_from_segment(self, signal):
        """
        :param signal:
        :return:
        """
        chroma_stft_mean = np.mean(librosa.feature.chroma_stft(y=signal))
        chroma_stft_var = librosa.feature.chroma_stft(y=signal).var()
        rms_mean = np.mean(librosa.feature.rms(y=signal))
        rms_var = librosa.feature.rms(y=signal).var()
        spectral_centroid_mean = np.mean(
            librosa.feature.spectral_centroid(y=signal))
        spectral_centroid_var = librosa.feature.spectral_centroid(y=signal).var()
        spectral_bandwidth_mean = np.mean(
            librosa.feature.spectral_bandwidth(y=signal))
        spectral_bandwidth_var = librosa.feature.spectral_bandwidth(
            y=signal).var()
        spectral_rolloff_mean = np.mean(
            librosa.feature.spectral_rolloff(y=signal))
        spectral_rolloff_var = librosa.feature.spectral_rolloff(y=signal).var()
        zero_crossing_rate_mean = np.mean(
            librosa.feature.zero_crossing_rate(y=signal))
        zero_crossing_rate_var = librosa.feature.zero_crossing_rate(
            signal).var()
        harmonic_mean = np.mean(librosa.effects.harmonic(y=signal))
        harmonic_var = librosa.effects.harmonic(y=signal).var()
        _, y_perceptr = librosa.effects.hpss(y=signal)
        perceptr_mean = np.mean(y_perceptr).real
        perceptr_var = y_perceptr.var()
        tempo, _ = librosa.beat.beat_track(y=signal)

        mfcc = self._extract_mfcc_feature(signal)
        mfcc_mean = [np.mean(m) for m in mfcc]
        mfcc_var = [m.var() for m in mfcc]
        mfcc_data = []
        for mean, var in zip(mfcc_mean, mfcc_var):
            mfcc_data = np.append(mfcc_data, mean)
            mfcc_data = np.append(mfcc_data, var)

        data = np.array(
            [self.duration,
             chroma_stft_mean,
             chroma_stft_var,
             rms_mean,
             rms_var,
             spectral_centroid_mean,
             spectral_centroid_var,
             spectral_bandwidth_mean,
             spectral_bandwidth_var,
             spectral_rolloff_mean,
             spectral_rolloff_var,
             zero_crossing_rate_mean,
             zero_crossing_rate_var,
             harmonic_mean,
             harmonic_var,
             perceptr_mean,
             perceptr_var,
             tempo
             ])

        data = np.concatenate((data, mfcc_data))
        return data

    def _extract_and_format_mfcc_feature_from_segment(self, signal):
        num_mfcc_vectors_per_segment = math.ceil(
            self.samples_per_segment / self.hop_length)
        mfcc = self._extract_mfcc_feature(signal, 13)
        mfcc = mfcc.T
        mfcc_data = []
        if len(mfcc) == num_mfcc_vectors_per_segment:
            mfcc_data.append(mfcc.tolist())

        return mfcc.tolist()

    def _extract_mfcc_feature(self, signal, n_mfcc: int = 20):
        return librosa.feature.mfcc(y=signal,
                                    sr=self.sample_rate,
                                    S=None,
                                    n_mfcc=n_mfcc,
                                    dct_type=2,
                                    norm="ortho",
                                    lifter=0)
