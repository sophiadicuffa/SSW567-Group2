''' Test 5 - 907 - https://chat.openai.com/share/bbf03be2-dc7b-4451-a614-1a542af33712 '''

import PySimpleGUI as sg
from googletrans import Translator, LANGUAGES

def translate_text(text, target="en"):
    translator = Translator()
    translation = translator.translate(text, dest=target)
    return translation.text

def create_window():
    sg.theme('LightGreen')

    layout = [
        [sg.Text('Choose a language to translate to:'),
         sg.Combo(list(LANGUAGES.values()), key='-LANG-', size=(20, 1))],
        [sg.Text('Enter text to translate:'),
         sg.InputText(key='-TEXT-', size=(50, 5))],
        [sg.Button('Translate'), sg.Button('Exit')],
        [sg.Text('Translation output:', size=(40, 1))],
        [sg.Output(size=(60, 10), key='-OUTPUT-')]
    ]

    return sg.Window('Text Translator', layout, font=('Helvetica', 14))

def main():
    window = create_window()

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break

        if event == 'Translate':
            target_language_key = {v: k for k, v in LANGUAGES.items()}[values['-LANG-']]
            translated_text = translate_text(values['-TEXT-'], target=target_language_key)
            print(translated_text)

    window.close()

if __name__ == '__main__':
    main()
