import os
from flask import Flask
from flask import render_template, redirect, request
#from .model.inference import label


app = Flask(__name__)

IMAGE_UPLOADS = 'webapp/app/static/uploads/'

@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == "POST":
		if request.files:
			image = request.files["image"]
			# save the uploaded image for viewing
			image.save(os.path.join(IMAGE_UPLOADS, image.filename))

			print("Image Uploaded")

			return redirect(request.url)

	return render_template('index.html')


if __name__ == '__main__':
	app.run(debug=True)
