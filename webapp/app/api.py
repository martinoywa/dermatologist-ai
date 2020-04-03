import os

from flask import Blueprint, render_template, redirect, request
#from .model.inference import label


main = Blueprint('main', __name__)

IMAGE_UPLOADS = 'webapp/app/static/uploads/'

@main.route('/', methods=['GET', 'POST'])
def home():
	if request.method == "POST":
		if request.files:
			image = request.files["image"]
			# save the uploaded image for viewing
			image.save(os.path.join(IMAGE_UPLOADS, image.filename))

			print("Image Uploaded")

			return redirect(request.url)

	return render_template('index.html')
