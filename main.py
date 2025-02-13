from flask import Flask,render_template, request
import os
import fal_client
import requests
import time

os.environ["FAL_KEY"] = 'your-api-key'

app = Flask(__name__)

def generateImage(garmentLocation):
    urlHuman = fal_client.upload_file(r"human_images_uploaded\human_image.jpg")
    urlGarment = fal_client.upload_file(garmentLocation)

    handler = fal_client.submit(
        "fal-ai/idm-vton",
        arguments={
            "human_image_url": urlHuman,
            "garment_image_url": urlGarment,
            "description": "Short Sleeve Round Neck T-shirts"
        },
    )

    result = handler.get()
    print(result)

    img_data = requests.get(result['image']["url"]).content
    with open('static/final.jpg', 'wb') as handler:
        handler.write(img_data)

    time.sleep(1)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/garment', methods=['POST'])
def loading():
    if request.method == 'POST':   
        f = request.files['file']
        if not os.path.exists('human_images_uploaded'):
            os.makedirs('human_images_uploaded')
        f.save(f"human_images_uploaded/human_image.jpg")
    return render_template('garment_upload.html')

@app.route('/final', methods=['POST'])
def generate_image():
    if request.method == 'POST':   
        f = request.files['file']
        if not os.path.exists('garment_images_uploaded'):
            os.makedirs('garment_images_uploaded')
        f.save(f"garment_images_uploaded/{f.filename}")

    generateImage(f"garment_images_uploaded/{f.filename}")
    return render_template('final.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True, port=1000)