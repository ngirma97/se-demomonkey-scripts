from http.server import BaseHTTPRequestHandler
import os

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. SECURITY CHECK
        # This ensures random people can't trigger your script by visiting the URL
        auth_header = self.headers.get('Authorization')
        cron_secret = os.environ.get('CRON_SECRET')

        # Only check security if CRON_SECRET is set in Vercel Environment Variables
        if cron_secret and auth_header != f"Bearer {cron_secret}":
            self.send_response(401)
            self.end_headers()
            self.wfile.write("Unauthorized".encode('utf-8'))
            return

        # 2. YOUR LOGIC
        print("hello")  # This goes to the Vercel Logs
        
        # You can add more logic here later
        # e.g., my_function()

        # 3. SEND RESPONSE TO VERCEL
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write("Script ran successfully: hello printed to logs".encode('utf-8'))
        return