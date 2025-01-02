import os
import time
import requests
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import base64

# creds config
Websites = ['https://www.google.com', 'https://www.facebook.com', 'https://youtube.com']
check_interval = 43200

# creds gmail
SCOPES = ['https://www.googleapis.com/auth/gmail.send']
creds = None
CREDENTIALS_FILE = #complete_path_to_credentials_file

def send_email_alert(site_url, status_code):
    """Função para enviar o alerta por email utilizando a API do Gmail"""
    subject = f"[ALERTA] {site_url} está fora do ar!"
    body = f"O site {site_url} retornou o código com o status {status_code}.\nVerificar o problema urgentemente."

    message = MIMEMultipart()
    message['From'] = #email_sender
    message['To'] = #email_receiver
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        service = build('gmail', 'v1', credentials=creds)
        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        message = service.users().messages().send(userId="me", body={'raw': raw_message}).execute()
        print(f"Email enviado com sucesso! ID: {message['id']}")
    except Exception as error:
        print(f"Erro ao enviar email: {error}")

def check_sites():
    for website in Websites:
        try:
            response = requests.get(website, timeout=10)
            if response.status_code == 200:
                print(f"{website} está online. Código: {response.status_code}")
            else:
                print(f"Problema detectado em {website}! Código: {response.status_code}")
                send_email_alert(website, response.status_code)
        except requests.RequestException as e:
            print(f"Erro ao acessar {website}: {e}")
            send_email_alert(website, "Indisponível")

def authenticate():
    global creds
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

def main():
    authenticate()
    while True:
        check_sites()
        time.sleep(check_interval)

if __name__ == "__main__":
    main()
