import requests
import io
import zipfile


def urlzipextract(zip_file_url):

	r = requests.get(zip_file_url)
	z = zipfile.ZipFile(io.BytesIO(r.content))
	z.extractall()
