import gradio as gr

from src.app.api.api_rest import predict_genre_music


def predict(audio_file):
    audio_array = audio_file[1]
    prediction = predict_genre_music(audio_array)
    return prediction


"""
with gr.Blocks() as demo:
    gr.Markdown("Music Genre Classification")

    with gr.Tab("Upload audio"):
        raw_audio_input = gr.Audio()
        raw_audio_output = gr.Textbox("Music Genre Predicted")
        raw_audio_button = gr.Button("Predict")

    with gr.Tab("Record audio"):
        record_audio_input = gr.inputs.Audio(source="microphone", type="filepath", optional=True, label="Music Recorder")
        record_audio_output = gr.Textbox()
        record_audio_button = gr.Button("Predict")

    record_audio_button.click(predict, inputs=record_audio_input, outputs=record_audio_output)
    raw_audio_button.click(predict, inputs=raw_audio_input, outputs=raw_audio_output)
"""

demo = gr.Interface(
    fn=predict,
    inputs=gr.Audio(),
    outputs = gr.Label(),
    allow_flagging="never"
    #examples=[
    #     [os.path.join(os.path.dirname(__file__),"audio/recording1.wav")],
    #    [os.path.join(os.path.dirname(__file__),"audio/cantina.wav")],
    # ],
)

demo.launch()
