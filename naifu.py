import base64
import random
import requests

headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15",
}

url = "https://focused-reservation-painted-dinner.trycloudflare.com/generate-stream"

def generate(prompt):
    prompt = "masterpiece, best quality," + prompt
    data = {
            "prompt":prompt,
            "width":512,
            "height":768,
            "scale":12,
            "sampler":"k_euler_ancestral",
            "steps":28,
            "seed":random.randint(0, 4294967295),
            "n_samples":1,
            "ucPreset":0,
            "uc":"lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry",
    }

    try:
        resp = requests.post(url, headers = headers, json = data)
        if resp.status_code == 200:
            img64 = resp.text.split("data:")[1]
            return base64.b64decode(img64)
        else:
            print(resp.status_code)
            return None
    except Exception as e:
        print(e)
        return None
