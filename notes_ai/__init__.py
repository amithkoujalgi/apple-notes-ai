import os
from pathlib import Path

HOME_DIR = str(Path.home())
NOTES_AI_DATA_DIR = os.path.join(HOME_DIR, '.notes-ai')
os.makedirs(NOTES_AI_DATA_DIR, exist_ok=True)
HUGGING_FACE_EMBEDDINGS_DEVICE_TYPE = 'cpu'
