import gradio as gr

from src.app.api.api_rest import predict_genre_music


def predict(audio_file):
    audio_array = audio_file[1]
    prediction = predict_genre_music(audio_array)
    return prediction


demo = gr.Interface(
    fn=predict,
    inputs=gr.Audio(),
    outputs=gr.Label(),
    allow_flagging="never"
    # examples=[
    #     [os.path.join(os.path.dirname(__file__),"audio/recording1.wav")],
    #    [os.path.join(os.path.dirname(__file__),"audio/cantina.wav")],
    # ],
)

demo.launch()
