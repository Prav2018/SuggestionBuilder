from flask import Flask, render_template, request, json
# from auto import run
from word_based import run
app =Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/search", methods=['GET'])
def getSuggestions():
    if request.method == 'GET':
        data = request.args.get('text')
        res={}
        res['data']= run(data)
        return json.dumps(res)

if __name__ == "__main__":
    app.run()


