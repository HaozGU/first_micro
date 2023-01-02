from flask import Flask
import requests
import google.auth
from googleapiclient.discovery import build

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


# Set the scopes and key file location for the Analytics API
VIEW_ID = '281161150'
SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = 'D:\5A s1\Data source\first_micro\digital-trace-lab-774d1ef2433e.json'


@app.route('/OAuth', methods=["GET"])
def OAuth():
    # Get the service account credentials
    credentials, _ = google.auth.default(scopes=SCOPES)

    # Build the Analytics API service
    service = build('analytics', 'v4', credentials=credentials)

    # Make a request to the Analytics API to fetch the number of visitors
    response = service.data().realtime().get(
        ids='ga:' + VIEW_ID,
        metrics='rt:activeUsers'
    ).execute()

    # Extract the number of visitors from the response
    visitors = response['totalsForAllResults']['rt:activeUsers']

    return f'Number of visitors: {visitors}'