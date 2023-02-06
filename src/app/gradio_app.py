from enum import Enum

import gradio
import httpx
import os


class ModelAllowed(Enum):
    GAUSSIAN_NB = 'Gaussian NB'
    RANDOM_FOREST = 'Random Forest'
    CNN = 'CNN'


async def predict(audio_file):
    client = httpx.AsyncClient()
    audio_array = audio_file[1]
    body = {'audio_array': audio_array.tolist(),
            'gtzan_model': ModelAllowed.RANDOM_FOREST.value,
            'mfcc_model': ModelAllowed.CNN.value}
    url = os.getenv('API_URL', 'http://localhost:8000/predict-music')
    response = await client.post(url, json=body, timeout=120)
    return response.text


demo = gradio.Interface(
    fn=predict,
    inputs=gradio.Audio(),
    outputs=gradio.Label(label='Predicted Genre'),
    allow_flagging='never',
    title='Music Genre Classification',
    description='This is a Music Genre Classification model based on a novel ensemble approach'
)

demo.launch(share=False, server_name='0.0.0.0')
