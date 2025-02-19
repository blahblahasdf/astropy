from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    """Return a simple hello world message."""
    return "Hello, World from Flask!"

def main():
    app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == "__main__":
    main()
