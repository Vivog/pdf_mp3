import pdfplumber
from gtts import gTTS
from pathlib import Path
def pdf_mp3(file_path='test.pdf', lang='en'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        print(f'---Load file is {Path(file_path).name}---')
        print('---Processing...---')
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)
        text = text.replace('\n', '')

        audio = gTTS(text, lang, slow=False)
        file_name = Path(file_path).stem
        audio.save(f'{file_name}.mp3')
        return f'---Operation is done---\n---{file_name}.mp3 save successfully---'

    else:
        return("File is not exists, check the file path")

def main():
    path = input('Please enter file path:')
    lang = input('Please enter file text language, for example \'en\' or \'ru\':')
    print(pdf_mp3(path, lang))

if __name__ == "__main__":
    main()



