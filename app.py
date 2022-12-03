

from flask import Flask

app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello_world():
    return "Hello World123"
    
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

 return prefix_google + "Hello World1234"