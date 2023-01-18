from enum import Enum

import gradio as gr
import httpx


class ModelAllowed(Enum):
    GAUSSIAN_NB = 'Gaussian NB'
    RANDOM_FOREST = 'Random Forest'
    CNN = 'CNN'


async def predict(audio_file):
    client = httpx.AsyncClient()
    audio_array = audio_file[1]
    body = {"audio_array": audio_array.tolist(),
            "gtzan_model": ModelAllowed.RANDOM_FOREST.value,
            "mfcc_model": ModelAllowed.CNN.value}
    response = await client.post("http://host.docker.internal:8000/predict_music", json=body, timeout=20)
    return response.text


demo = gr.Interface(
    fn=predict,
    inputs=gr.Audio(),
    outputs=gr.Label(),
    allow_flagging="never"
)

demo.launch(share=False, server_name="0.0.0.0")

# import pandas as pd

# def predict(audio_file):
#    audio_array = audio_file[1]
#    prediction = predict_genre_music(audio_array)
#    return prediction
