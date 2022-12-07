from flask import Flask
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route('/logger', methods=['GET'])
def logger():
    logging.info('This is a log message')
    return 'This is a log message'
    
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

# if __name__ == '__main__':
#     app.run()