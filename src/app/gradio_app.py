from enum import Enum

import gradio as gr
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
    url = os.getenv('API_URL')
    print(url)
    response = await client.post(url, json=body, timeout=20)
    return response.text


demo = gr.Interface(
    fn=predict,
    inputs=gr.Audio(),
    outputs=gr.Label(label='Predicted Genre'),
    allow_flagging='never',
    title='Music Genre Classification',
    description='This is a Music Genre Classification trained on GTZAN dataset and based on a novel ensemble approach'
)

demo.launch(debug=True, share=False, server_name='0.0.0.0')
