import requests
from pathlib import Path

output_dir = Path("downloaded_files")
filename = "thinkpython.pdf"
url = "https://greenteapress.com/thinkpython2/thinkpython2.pdf"

file_path = Path(output_dir) / filename


def download_file(url: str, file_path: Path):
    response = requests.get(url)
    response.raise_for_status() 

    file_path.write_bytes(response.content)

if not file_path.exists():
    download_file(url, file_path)