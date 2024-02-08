from nltk import word_tokenize
from string import punctuation
from pickle import *
from flask import *


# clean the data
def clean_data(txt):
    txt = txt.lower()
    txt = word_tokenize(txt)
    txt = [t for t in txt if t not in punctuation]
    txt = " ".join(txt)
    return txt


# model
f = open("model_all.pkl", "rb")
model = load(f)
f.close()

# cv
f = open("cv_all.pkl", "rb")
cv = load(f)
f.close()

app = Flask(__name__)


@app.route("/")
def home():
    if request.args.get("txt"):
        txt = request.args.get("txt")
        txt = clean_data(txt)
        ctxt = cv.transform([txt])
        ans = model.predict(ctxt)[0]
        return render_template("home.html", msg=ans)
    else:
        return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
