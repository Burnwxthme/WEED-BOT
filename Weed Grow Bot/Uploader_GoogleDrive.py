import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload



import os
os.chdir(r'c:\Users\Administrator\PythonPojects\Weed_Grow\Weed Grow Bot')


# OAuth 2.0 Scope (Zugriff auf Google Drive)
SCOPES = ['https://www.googleapis.com/auth/drive']

def authenticate():
    """Authentifiziert den Benutzer mit der Google Drive API."""
    creds = None
    try:
        # Prüfen, ob ein Token vorhanden ist (gespeicherte Anmeldedaten)
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        
        # Token ist entweder nicht vorhanden oder abgelaufen
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                # Falls kein gültiger Token existiert, starte den Anmeldeprozess
                flow = InstalledAppFlow.from_client_secrets_file(
    r'C:\Users\Administrator\PythonPojects\Weed_Grow\credentials.json', SCOPES)

                creds = flow.run_local_server(port=0)
            
            # Speichere das Token für zukünftige Verwendung
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
    except Exception as e:
        print(f"Fehler während der Authentifizierung: {e}")
    return creds

def create_drive_folder(service, folder_name):
    """Erstellt einen Ordner in Google Drive und gibt die Ordner-ID zurück."""
    try:
        file_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        folder = service.files().create(body=file_metadata, fields='id').execute()
        print(f"Ordner '{folder_name}' erstellt mit ID: {folder.get('id')}")
        return folder.get('id')
    except Exception as e:
        print(f"Fehler beim Erstellen des Ordners: {e}")
        return None

def upload_file(service, file_path, parent_folder_id):
    """Lädt eine Datei in einen bestimmten Google Drive-Ordner hoch."""
    try:
        file_metadata = {'name': os.path.basename(file_path), 'parents': [parent_folder_id]}
        media = MediaFileUpload(file_path, resumable=True)
        uploaded_file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        print(f"Datei '{file_path}' hochgeladen. File ID: {uploaded_file.get('id')}")
    except Exception as e:
        print(f"Fehler beim Hochladen der Datei '{file_path}': {e}")

def upload_folder(service, folder_path, parent_folder_id):
    """Lädt einen lokalen Ordner (inklusive Unterordner) in einen Google Drive-Ordner hoch."""
    try:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                upload_file(service, file_path, parent_folder_id)
    except Exception as e:
        print(f"Fehler beim Hochladen des Ordners '{folder_path}': {e}")

if __name__ == '__main__':
    # Lokalen Ordnerpfad und Google Drive-Ordnernamen festlegen
    local_folder_path = r'c:\Users\Administrator\PythonPojects\Weed_Grow\Weed Grow Bot'
    drive_folder_name = "Weed-bot-uploads"

    try:
        # Authentifizieren und Google Drive API-Service erstellen
        creds = authenticate()
        if creds:
            service = build('drive', 'v3', credentials=creds)

            # Google Drive-Ordner erstellen
            drive_folder_id = create_drive_folder(service, drive_folder_name)
            if drive_folder_id:
                # Lokalen Ordnerinhalt hochladen
                upload_folder(service, local_folder_path, drive_folder_id)
            else:
                print("Ordner konnte nicht erstellt werden.")
        else:
            print("Authentifizierung fehlgeschlagen.")
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
