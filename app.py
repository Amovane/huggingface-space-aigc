import os
import gradio as gr
import requests
openai_key = os.getenv("OPENAI_KEY")

def ganerate(prompt):
    n = 1
    size = "512x512"
    data = {"n": n, "prompt": prompt, "size": size}
    headers = {"Content-Type": "application/json",
               "Authorization": f"""Bearer {openai_key}"""}
    result = requests.post(
        "https://api.openai.com/v1/images/generations", json=data, headers=headers)
    return result.json()["data"][0]["url"]

iface = gr.Interface(
    fn=ganerate,
    inputs=[
        gr.Textbox(placeholder="Prompt", label="Prompt"),
    ],
    outputs="image")
iface.launch()
