#начни тут создавать приложение с умными заметками
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

import json
name = ''
tag = ''
tags = list()
search_result = dict()

def getTestNotes():
    return {
    'Добро пожаловать': {
        'text': 'В этой программе вы можете писать свои заметки!',
        'tags': ["новая", "пример"]
        }
    }
'''notes = getTestNotes()
with open('notes.json', 'w', encoding='utf-8') as file:
   json.dump(notes, file, ensure_ascii=False)'''
notes = {}
def add_note():
    note_name, ok = QInputDialog.getText(main_menu, 'Добавить заметку', 'Название заметки: ')
    while note_name == '':
        if ok == False:
            break
        note_name, ok = QInputDialog.getText(main_menu, 'Добавить заметку', 'Вы не ввели название заметки!!! Введите название заметки: ')
    if ok == True:
        notes[note_name] = {'text': '',
        'tags': []}
        lw_list_notes.addItem(note_name)
        te_text_note.setText('')
def save_note():
    global name
    try:
        notes[name]['text'] = te_text_note.toPlainText()
        with open('notes.json', 'w', encoding='utf-8') as file:
            json.dump(notes, file, ensure_ascii=False)
    except:
        msg = QMessageBox()
        msg.setText('Вы не выбрали заметку(скопируйте текст и выберете заметку)!!!')
        msg.exec_()
#save_note()

def load_notes():
    try:
        with open('notes.json', 'r', encoding='utf-8') as file:
            global notes
            notes = json.load(file)
    except:
        with open('notes.json', 'w', encoding='utf-8') as file:
            notes = getTestNotes()
            json.dump(notes, file, ensure_ascii=False)
load_notes()
def show_note():
    global name
    name = lw_list_notes.selectedItems()[0].text()
    #print(notes[name]['текст'])
    #print(notes[name])
    #print(name)
    te_text_note.setText(notes[name]['text'])
    lw_list_tags.clear()
    lw_list_tags.addItems(notes[name]['tags'])
def delete_note():
    global name
    try:
        del notes[name]
        lw_list_notes.clear()
        lw_list_notes.addItems(notes.keys())
        te_text_note.clear()
        lw_list_tags.clear()
        with open('notes.json', 'w', encoding='utf-8') as file:
            json.dump(notes, file, ensure_ascii=False)
    except:
        msg = QMessageBox()
        msg.setText('Вы не выбрали заметку!!!')
        msg.exec_()
def selectTag():
    global tag
    tag = lw_list_tags.selectedItems()[0].text()
def create_tag():
    global name
    global notes
    if le_tag.text() != '':
        if name != '':
            data = le_tag.text()
            data = data.lower()
            if data in notes[name]['tags']:
                msg = QMessageBox()
                msg.setText('Такой тег уже есть!!!')
                msg.exec_()
            else:
                lw_list_tags.addItem(data)
                notes[name]['tags'].append(data)
                le_tag.setText('')
        else:
            msg2 = QMessageBox()
            msg2.setText('Вы не выбрали заметку!!!')
            msg2.exec_()
    else:
        msg = QMessageBox()
        msg.setText('Вы не ввели тег!!!')
        msg.exec_()
def delete_tag():
    global tag
    if tag != '':
        notes[name]['tags'].remove(tag)
        lw_list_tags.clear()
        lw_list_tags.addItems(notes[name]['tags'])
        with open('notes.json', 'w', encoding='utf-8') as file:
            json.dump(notes, file, ensure_ascii=False)
    else:
        msg = QMessageBox()
        msg.setText('Вы не выбрали тег!!!')
        msg.exec_()

def search_notes():
    data_list = list()
    tag = le_tag.text()
    tag = tag.lower()
    if btn_search_to_note.text() == 'Искать заметки по тегу':
        btn_search_to_note.setText('Сбросить результаты поиска')
        gb_notes.setTitle('Результаты поиска')
        lw_list_notes.clear()
        lw_list_tags.clear()
        data_list = notes.keys()
        print(data_list)
        for key in range(len(data_list) - 1):
            if tag in notes[data_list[key]]['tags']:
                search_result[data_list[key]] = notes[data[key]]
    elif btn_search_to_note.text() == 'Сбросить результаты поиска':
        btn_search_to_note.setText('Искать заметки по тегу')
        gb_notes.setTitle('Список заметок')
        lw_list_notes.addItems(notes.keys())
#notes = {}
#load_notes()
app = QApplication([])
main_menu = QWidget()
main_menu.setWindowTitle('Умные заметки')

te_text_note = QTextEdit()
lw_list_notes = QListWidget()
btn_create_note = QPushButton('Создать заметку')
btn_remove_note = QPushButton('Удалить заметку')
btn_save_note = QPushButton('Сохранить заметку')
lw_list_tags = QListWidget()
le_tag = QLineEdit()
btn_add_to_note = QPushButton('Добавить к заметке')
btn_remove_to_note = QPushButton('Открепить от заметки')
btn_search_to_note = QPushButton('Искать заметки по тегу')

gb_notes = QGroupBox('Список заметок')
lw_list_notes.addItems(notes.keys())
te_text_note.setPlaceholderText('Здесь можно писать текст\nС уважением, Никита Речкин\n')
le_tag.setPlaceholderText('Введите тег...')
gb_notes__Main_VLayout = QVBoxLayout()
gb_notes__HLayout1 = QHBoxLayout()
gb_notes__HLayout2 = QHBoxLayout()
gb_notes__HLayout3 = QHBoxLayout()

gb_notes__HLayout1.addWidget(lw_list_notes, alignment=Qt.AlignCenter)
gb_notes__HLayout2.addWidget(btn_create_note, alignment=Qt.AlignCenter)
gb_notes__HLayout2.addWidget(btn_remove_note, alignment=Qt.AlignCenter)
gb_notes__HLayout3.addWidget(btn_save_note, alignment=Qt.AlignCenter, stretch=15)
gb_notes__Main_VLayout.addLayout(gb_notes__HLayout1)
gb_notes__Main_VLayout.addLayout(gb_notes__HLayout2)
gb_notes__Main_VLayout.addLayout(gb_notes__HLayout3)
gb_notes.setLayout(gb_notes__Main_VLayout)

gb_tags = QGroupBox('Список тегов')
gb_tags__MainVLayout = QVBoxLayout()
gb_tags__HLayout1 = QHBoxLayout()
gb_tags__HLayout2 = QHBoxLayout()
gb_tags__HLayout3 = QHBoxLayout()
gb_tags__HLayout4 = QHBoxLayout()

gb_tags__HLayout1.addWidget(lw_list_tags, alignment=Qt.AlignCenter)
gb_tags__HLayout2.addWidget(le_tag, alignment=Qt.AlignCenter, stretch=20)
gb_tags__HLayout3.addWidget(btn_add_to_note, alignment=Qt.AlignCenter)
gb_tags__HLayout3.addWidget(btn_remove_to_note, alignment=Qt.AlignCenter)
gb_tags__HLayout4.addWidget(btn_search_to_note, alignment=Qt.AlignCenter, stretch = 5)
gb_tags__MainVLayout.addLayout(gb_tags__HLayout1)
gb_tags__MainVLayout.addLayout(gb_tags__HLayout2)
gb_tags__MainVLayout.addLayout(gb_tags__HLayout3)
gb_tags__MainVLayout.addLayout(gb_tags__HLayout4)

gb_tags.setLayout(gb_tags__MainVLayout)

MainHLayout = QHBoxLayout()
VLayout1 = QVBoxLayout()
VLayout2 = QVBoxLayout()

VLayout1.addWidget(te_text_note)
VLayout2.addWidget(gb_notes, alignment=Qt.AlignCenter)
VLayout2.addWidget(gb_tags, alignment=Qt.AlignCenter)

MainHLayout.addLayout(VLayout1)
MainHLayout.addLayout(VLayout2)
main_menu.setLayout(MainHLayout)

#create_note()
lw_list_notes.itemClicked.connect(show_note)
btn_create_note.clicked.connect(add_note)
btn_save_note.clicked.connect(save_note)
btn_remove_note.clicked.connect(delete_note)
btn_add_to_note.clicked.connect(create_tag)
lw_list_tags.itemClicked.connect(selectTag)
btn_remove_to_note.clicked.connect(delete_tag)
btn_search_to_note.clicked.connect(search_notes)

main_menu.resize(500, 300)
main_menu.show()
app.setStyle('Fusion')
#QStyleFactory.create
app.exec_()