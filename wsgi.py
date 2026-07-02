from waitress import serve
from app import app
import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    print(f"Starting ParkEase production server on port {port}...")
    print(f"Access at: http://localhost:{port}")
    serve(app, host='0.0.0.0', port=port)