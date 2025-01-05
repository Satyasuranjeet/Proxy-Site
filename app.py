from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Proxy Site</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f9;
                    margin: 0;
                    padding: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }
                .container {
                    text-align: center;
                    background: white;
                    padding: 20px 40px;
                    border-radius: 10px;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                }
                h1 {
                    font-size: 24px;
                    margin-bottom: 10px;
                }
                form {
                    margin-top: 20px;
                }
                input[type="text"] {
                    width: 300px;
                    padding: 10px;
                    border: 1px solid #ddd;
                    border-radius: 5px;
                    font-size: 16px;
                }
                button {
                    padding: 10px 20px;
                    background-color: #007bff;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    font-size: 16px;
                    cursor: pointer;
                }
                button:hover {
                    background-color: #0056b3;
                }
                footer {
                    margin-top: 20px;
                    font-size: 12px;
                    color: #777;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Welcome to Proxy Site</h1>
                <p>Enter the URL of the site you want to access below:</p>
                <form method="GET" action="/proxy">
                    <input type="text" name="url" placeholder="https://example.com" required>
                    <button type="submit">Go</button>
                </form>
                <footer>
                    <p>&copy; 2025 Proxy Site. Use responsibly.</p>
                </footer>
            </div>
        </body>
        </html>
    '''

@app.route('/proxy')
def proxy():
    url = request.args.get('url')
    if not url.startswith("http"):
        url = "http://" + url
    try:
        resp = requests.get(url)
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
        return Response(resp.content, resp.status_code, headers)
    except Exception as e:
        return f"<p style='color:red;'>Error: {e}</p>"

if __name__ == "__main__":
    app.run(debug=True)
