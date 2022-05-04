from gtts import gTTS
import pdfplumber
from pathlib import Path
from art import tprint

def pdf_to_mp3(file_path, language='en'):
      if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
            # return 'File exists'
            with pdfplumber.PDF(open(file_path, 'rb')) as pdf:
                pages = [page.extract_text() for page in pdf.pages]
            text = ''.join(pages).replace('\n', '')
            audio = gTTS(text=text, lang=language, slow=False)
            file_name = 'Result.mp3'
            audio.save(file_name)

            return f'{file_name} saved successfully!'

      else:
            return 'File not exists or not PDF format! Chech the file path'

def main():
      tprint('PDF -> MP3', font='bulbhead')
      print(pdf_to_mp3('Test.pdf'))

if __name__ == "__main__":
      main()