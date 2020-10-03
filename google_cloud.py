from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload,MediaFileUpload
from googleapiclient.discovery import build
import pprint
import io

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = '/Users/79185/Downloads/reglament-112fdcb73dd9.json'

credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('drive', 'v3', credentials=credentials)

results = service.files().list(pageSize=10,
                               fields="nextPageToken, files(id, name, mimeType)").execute()

print(results)


def download_files_from(file_id='1m3zb9pVJ470Z-rQYPHfEgm7WwIFfNUUv', filename='/Users/79185/PycharmProjects/Reglament/PIL (2).txt'):
    file_id = file_id
    request = service.files().get_media(fileId=file_id)
    filename = filename
    fh = io.FileIO(filename, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))


def download_files_to(folder_id='1ierobuM_NbwuNZIiKgu34xnSRMoxI-Ra', name='Test.py'):
    folder_id = folder_id
    name = name
    file_path = '/Users/79185/PycharmProjects/Reglament/google_cloud.py'
    file_metadata = {
        'name': name,
        'parents': [folder_id]
    }
    media = MediaFileUpload(file_path, resumable=True)
    r = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(r)


download_files_to()