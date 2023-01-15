import gradio as gr
import numpy as np
from scipy.io.wavfile import write


def save_file(audio_array):
    rate = 22050
    scaled = np.int16(audio_array / np.max(np.abs(audio_array)) * 32767)
    path_file = 'predict.wav'
    write(path_file, rate, scaled)


def predict(audio_file):
    print(audio_file)
    print(type(audio_file[1]))
    save_file(audio_file[1])


with gr.Blocks() as demo:
    gr.Markdown("Music Genre Classification")

    with gr.Tab("Record audio"):
        record_audio_input = gr.Audio()
        record_audio_output = gr.Textbox()
        record_audio_button = gr.Button("Predict")

    with gr.Tab("Upload audio"):
        raw_audio_input = gr.inputs.Audio(source="microphone", type="filepath", optional=True, label="Music Recorder")
        raw_audio_output = gr.Textbox()
        raw_audio_button = gr.Button("Predict")

    record_audio_button.click(predict, inputs=record_audio_input, outputs=record_audio_output)
    raw_audio_button.click(predict, inputs=raw_audio_input, outputs=raw_audio_output)

demo.launch(debug=False)
