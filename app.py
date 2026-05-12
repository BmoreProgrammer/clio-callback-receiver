"""
app.py — OAuth callback receiver for Clio
Deployed on Vercel as a Serverless Function.
Receives the ?code= parameter from Clio OAuth redirect and displays it.
"""

from flask import Flask, request

app = Flask(__name__)

PAGE = """<!DOCTYPE html>
<html>
<head>
    <title>Clio OAuth Callback</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 700px; margin: 60px auto; padding: 20px; }
        h1 { color: #2c3e50; }
        .box { background: #f8f9fa; border: 1px solid #dee2e6; border-radius: 8px;
               padding: 24px; margin: 20px 0; }
        .code { background: #1e1e1e; color: #d4d4d4; padding: 16px; border-radius: 6px;
                font-family: monospace; word-break: break-all; font-size: 13px; }
        .label { font-weight: bold; color: #495057; margin-bottom: 8px; }
        .ok { color: #28a745; }
        .error { color: #dc3545; }
    </style>
</head>
<body>
    <h1>Clio OAuth Callback</h1>
    <div class="box">
        <div class="label">Authorization Code:</div>
        <div class="code" id="code">Loading...</div>
    </div>
    <div id="status" class="box"></div>
    <div class="box">
        <div class="label">Next Steps</div>
        <ol>
            <li>Copy the code above</li>
            <li>Come back to this chat and paste it</li>
            <li>I'll exchange it for your Clio access token</li>
        </ol>
    </div>
    <script>
        const params = new URLSearchParams(window.location.search);
        var code = params.get('code');
        var error = params.get('error');

        if (error) {
            document.getElementById('code').textContent = 'ERROR: ' + error;
            document.getElementById('code').style.color = '#dc3545';
            document.getElementById('status').innerHTML = '<span class="error">Error: ' + error + '</span>';
        } else if (code) {
            document.getElementById('code').textContent = code;
            document.getElementById('status').innerHTML = '<span class="ok">SUCCESS - Code received!</span>';
        } else {
            document.getElementById('code').textContent = 'No code in URL - visit the authorization URL first.';
            document.getElementById('code').style.color = '#856404';
            document.getElementById('code').style.background = '#fff3cd';
        }
    </script>
</body>
</html>"""

@app.route("/")
def index():
    return PAGE

@app.route("/callback")
def callback():
    return PAGE
