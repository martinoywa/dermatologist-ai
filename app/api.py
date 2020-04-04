import os
from flask import Flask
from flask import render_template, redirect, request
from werkzeug.utils import secure_filename
#from .model.inference import label


app = Flask(__name__)

# configurations
app.config["IMAGE_UPLOADS"] = "app/static/uploads/"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG"]

if 'uploads' not in os.listdir('app/static'):
	os.mkdir(app.config["IMAGE_UPLOADS"])	# make the uploads folder

def allowed_image(filename):
	if "." not in filename:
		return False

	extension = filename.rsplit(".", 1)[1]	# get extension

	if extension.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
		return True
	return False

@app.route("/", methods=["GET", "POST"])
def home():
	if request.method == "GET":
		return render_template("index.html")

	if request.method == "POST":
		if request.files:
			image = request.files["image"]

			if image.filename == "":	# No filename
				return redirect(request.url)

			if allowed_image(image.filename):
				filename = secure_filename(image.filename)
				image.save(os.path.join(app.config["IMAGE_UPLOADS"],
							filename))	# File saved
			else:	# File not allowed
				return redirect(request.url)

	return render_template("result.html", filename=filename)


if __name__ == "__main__":
	app.run(debug=True)
