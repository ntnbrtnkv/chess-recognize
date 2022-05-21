from tkinter import *
from tkinter import messagebox
import sys
import webbrowser
from PIL import ImageGrab
from Exporter import LichessExporter

from Recognition import Recognition
from HyperlinkManager import HyperlinkManager
from resourse_path import resource_path

window = Tk()
window.iconbitmap(resource_path("icon.ico"))
window.title("Chess Recognize")

Grid.rowconfigure(window, 0, weight=0)
Grid.rowconfigure(window, 1, weight=1)
Grid.columnconfigure(window, 0, weight=1)

TMP_FILENAME = 'tmp.png'

def open_in_broswer(link):
    return lambda: webbrowser.open_new(link)

def imgps():
    try:
        im = ImageGrab.grabclipboard()
        im.save(TMP_FILENAME)
    except BaseException as err:
        messagebox.showinfo(message="Clipboard is Empty.")
        return

    try:
        fen, _, _ = Recognition.get_fen(TMP_FILENAME)
        lichess = LichessExporter(fen)
        print('Parsed FEN: {0}'.format(fen))

        w2m_link = lichess.white_to_move()
        b2m_link = lichess.black_to_move()

        add_links(w2m_link=w2m_link, b2m_link=b2m_link)

        print('=' * 80)
    except BaseException as err:
        redirector(str(err))

pbtn11 = Button(window, text="Parse from clipboard", command=imgps)
pbtn11.grid(row=0, sticky='nsew')

textbox=Text(window, font="TkFixedFont")
hyperlink = HyperlinkManager(textbox)
textbox.grid(row=1, sticky='nsew')

def add_links(w2m_link, b2m_link):
    textbox.insert(END, 'White to move: {0}'.format(w2m_link) + '\n', hyperlink.add(open_in_broswer(w2m_link)))

    textbox.insert(END, 'Black to move: {0}'.format(b2m_link) + '\n', hyperlink.add(open_in_broswer(b2m_link)))

def redirector(inputStr):
    textbox.insert(END, inputStr + '\n')

sys.stdout.write = redirector
print('Output')

window.mainloop()