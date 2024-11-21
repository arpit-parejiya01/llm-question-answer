from flask import Flask,request,jsonify
from app.utils.utils import chain

app = Flask(__name__)
@app.route("/")
def home():
  return jsonify({"hello":"Hello world"})

@app.route("/chat",methods = ["POST"])
def response():
  try :
    question = request.get_json()["question"]
    data = chain.invoke({"question":question})
    return jsonify({"javab":str(data)})
  except Exception as e:
    print(e)
    
if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=5000)