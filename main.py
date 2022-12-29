from flask import Flask
import requests

app = Flask(__name__)

@app.route('/', methods=["GET"])
# def hello_world():
#     return "Hello World"
    
def hello_world_google_tag():
 prefix_google = """
 <!-- Google tag (gtag.js) -->
<script async
src="https://www.googletagmanager.com/gtag/js?id=UA-250950046-4"></script>
<script>
 window.dataLayer = window.dataLayer || [];
 function gtag(){dataLayer.push(arguments);}
 gtag('js', new Date());
 gtag('config', 'UA-250950046-4');
</script>
 """
 return prefix_google + "Hello World"

@app.route('/logger', methods=["GET"])
def logger():
    print("This is a log message on the Python console")
    script = """
    <script>
    console.log("This is a log message displayed on the browser")
    </script>
    """
    return script

@app.route('/cookie', methods=["GET"])
def cookie():
    req = requests.get("https://www.google.com/")
    return req.cookies.get_dict()

@app.route('/report', methods=["GET"])
def report():
    req = requests.get("https://analytics.google.com/analytics/web/#/reporthome/a164062586w272485488p243020933")
    return req.text

