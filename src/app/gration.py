import gradio as gr
import httpx

from src.app.api.entities.model_allowed_enum import ModelAllowed


async def predict(audio_file):
    client = httpx.AsyncClient()
    audio_array = audio_file[1]
    body = {"audio_array": audio_array.tolist(),
            "gtzan_model": ModelAllowed.RANDOM_FOREST.value,
            "mfcc_model": ModelAllowed.CNN.value}
    response = await client.post("http://localhost:8000/predict_music", json=body, timeout=20)
    return response.text


demo = gr.Interface(
    fn=predict,
    inputs=gr.Audio(),
    outputs=gr.Label(),
    allow_flagging="never"
)

demo.launch(share=True)


# import pandas as pd

# def predict(audio_file):
#    audio_array = audio_file[1]
#    prediction = predict_genre_music(audio_array)
#    return prediction
