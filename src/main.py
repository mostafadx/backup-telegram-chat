import base64
from telethon import TelegramClient, sync
import os

# Function to download messages and media
def backup_chat(api_id, api_hash, phone_number, username, forward_to_username):
    try:
        # Initialize Telegram client
        client = TelegramClient('session', api_id, api_hash)
        client.start(phone=phone_number)

        # Get the chat
        chat = client.get_entity(username)

        for message in client.iter_messages(chat):
            
            try:
                client.forward_messages(forward_to_username, message)
            except Exception as e:
                pass

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Read API credentials from ENV Variables 
    PHONE_NUMBER = os.getenv("PHONE_NUMBER")
    API_ID = os.getenv("API_ID")
    API_HASH = os.getenv("API_HASH")

    # Chat username to back up from ENV Variable
    USERNAME = os.getenv("USERNAME")

    # get forward_to_username
    FORWARD_TO_USERNAME = os.getenv("FORWARD_TO_USERNAME")

    # Load session from ENV Variable
    session = os.getenv("SESSION")
    if session:
        with open("session.session", "wb") as session_file:
            session_file.write(base64.b64decode(session))

    # Perform the backup
    backup_chat(API_ID, API_HASH, PHONE_NUMBER, USERNAME, FORWARD_TO_USERNAME)
