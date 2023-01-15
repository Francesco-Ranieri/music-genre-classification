import librosa
import numpy as np
import pandas as pd
from scipy.io.wavfile import write
import os


class FeatureExtractor:
    num_segment = 10
    duration = 66149
    n_mfcc = 20
    n_fft = 2048
    hop_length = 512
    sample_rate = 22050
    track_duration = 30
    path_file = 'temp.wav'
    data = []
    columns = ['length', 'chroma_stft_mean', 'chroma_stft_var', 'rms_mean', 'rms_var', 'spectral_centroid_mean',
               'spectral_centroid_var', 'spectral_bandwidth_mean', 'spectral_bandwidth_var', 'rolloff_mean',
               'rolloff_var', 'zero_crossing_rate_mean', 'zero_crossing_rate_var', 'harmony_mean', 'harmony_var',
               'perceptr_mean', 'perceptr_var', 'tempo', 'mfcc1_mean', 'mfcc1_var', 'mfcc2_mean', 'mfcc2_var',
               'mfcc3_mean', 'mfcc3_var', 'mfcc4_mean', 'mfcc4_var', 'mfcc5_mean', 'mfcc5_var', 'mfcc6_mean',
               'mfcc6_var',
               'mfcc7_mean', 'mfcc7_var', 'mfcc8_mean', 'mfcc8_var', 'mfcc9_mean', 'mfcc9_var', 'mfcc10_mean',
               'mfcc10_var', 'mfcc11_mean', 'mfcc11_var', 'mfcc12_mean', 'mfcc12_var', 'mfcc13_mean', 'mfcc13_var',
               'mfcc14_mean', 'mfcc14_var', 'mfcc15_mean', 'mfcc15_var', 'mfcc16_mean', 'mfcc16_var', 'mfcc17_mean',
               'mfcc17_var', 'mfcc18_mean', 'mfcc18_var', 'mfcc19_mean', 'mfcc19_var', 'mfcc20_mean', 'mfcc20_var']

    def __init__(self):
        pass

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

        for segment in range(num_segment):
            sample_per_track = self.sample_rate * self.track_duration
            samples_per_segment = int(sample_per_track / 10)
            start = samples_per_segment * segment
            finish = start + samples_per_segment
            signal_split = signal[start:finish]
            self._extract_gtzan_feature_from_segment(signal_split)

        df = pd.DataFrame(data=self.data, columns=self.columns)
        # df = pd.DataFrame(data=self.data, columns=self.columns)
        return df

    def _extract_gtzan_feature_from_segment(self, signal):

        """
        :param signal:
        :return:
        """

        chroma_stft_mean = np.mean(librosa.feature.chroma_stft(signal))
        chroma_stft_var = librosa.feature.chroma_stft(signal).var()
        rms_mean = np.mean(librosa.feature.rms(signal))
        rms_var = librosa.feature.rms(signal).var()
        spectral_centroid_mean = np.mean(librosa.feature.spectral_centroid(signal))
        spectral_centroid_var = librosa.feature.spectral_centroid(signal).var()
        spectral_bandwidth_mean = np.mean(librosa.feature.spectral_bandwidth(signal))
        spectral_bandwidth_var = librosa.feature.spectral_bandwidth(signal).var()
        spectral_rolloff_mean = np.mean(librosa.feature.spectral_rolloff(signal))
        spectral_rolloff_var = librosa.feature.spectral_rolloff(signal).var()
        zero_crossing_rate_mean = np.mean(librosa.feature.zero_crossing_rate(signal))
        zero_crossing_rate_var = librosa.feature.zero_crossing_rate(signal).var()
        harmonic_mean = np.mean(librosa.effects.harmonic(signal))
        harmonic_var = librosa.effects.harmonic(signal).var()
        _, y_perceptr = librosa.effects.hpss(signal)
        perceptr_mean = np.mean(y_perceptr).real
        perceptr_var = y_perceptr.var()
        tempo, _ = librosa.beat.beat_track(signal)

        mfcc = librosa.feature.mfcc(signal,
                                    self.sample_rate,
                                    n_mfcc=self.n_mfcc,
                                    n_fft=self.n_fft,
                                    hop_length=self.hop_length)
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
        self.data.append(data)
