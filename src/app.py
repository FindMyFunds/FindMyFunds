from flask import Flask,render_template
import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore

cred = credentials.Certificate("../findmyfunds-abc6f-firebase-adminsdk-jbztg-8112e8391f.json")
firebase_admin.initialize_app(cred)
app = Flask(__name__)

store = firestore.client()

doc_ref = store.collection(u'websites')
doc_ref.add({u'url': u'www.canada.ca', u'title': u'ESDC', u'desc': u'helloooo'})

@app.route("/")
def main():
    return render_template('main.html')

@app.route("/dashboard")
def dashboard():
  return render_template("dashboard.html")

if __name__ == "__main__":
    app.run()