import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os

main_application = tk.Tk()
main_application.geometry('800x600')
main_application.title('TCC Editor - V.0.1')


########################### 1:50:21

###################### Main Menu ##########################################
#---------------------&&&&&&&& End Main Menu &&&&&&&&----------------------
main_menu = tk.Menu()

###########################  A R Q U I V O  ##################################################
#Icons
new_icon = tk.PhotoImage(file='icons/new.png')
open_icon = tk.PhotoImage(file='icons/open.png')
save_icon = tk.PhotoImage(file='icons/save.png')
save_as_icon = tk.PhotoImage(file='icons/save_as.png')
exit_icon = tk.PhotoImage(file='icons/exit.png')

#Add menu na barra
file = tk.Menu(main_menu, tearoff=False)

###########################  E D I T A R  ###################################################
#Icons
copy_icon = tk.PhotoImage(file='icons/copy.png')
paste_icon = tk.PhotoImage(file='icons/paste.png')
cut_icon = tk.PhotoImage(file='icons/cut.png')
clear_all_icon = tk.PhotoImage(file='icons/clear_all.png')
find_icon = tk.PhotoImage(file='icons/find.png')

#Add menu Editar na barra
edit = tk.Menu(main_menu, tearoff=False)

###########################  V I S U A L I Z A R  ##################################################
#Icons
tool_bar_icon = tk.PhotoImage(file='icons/tool_bar.png')
status_bar_icon = tk.PhotoImage(file='icons/status_bar.png')

#Add menu Visualizar na barra
view = tk.Menu(main_menu, tearoff=False)

###########################  C O L O R  T H E M E  ###################################################
#Icons
light_default_icon = tk.PhotoImage(file='icons/light_default.png')
light_plus_icon = tk.PhotoImage(file='icons/light_plus.png')
dark_icon = tk.PhotoImage(file='icons/dark.png')
red_icon = tk.PhotoImage(file='icons/red.png')
monokai_icon = tk.PhotoImage(file='icons/monokai.png')
night_blue_icon = tk.PhotoImage(file='icons/night_blue.png')

#Add menu Background na barra
color_theme = tk.Menu(main_menu, tearoff=False)

theme_choice = tk.StringVar()
color_icons = (light_default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)
color_dict = {
    'Light Default' : ('#000000', '#ffffff'),
    'Light Plus' : ('#474747', '#e0e0e0'),
    'Dark' : ('#c4c4c4', '#ffe8e8'),
    'Red' : ('#2d2d2d', '#ffe8e8'),
    'Monokai' : ('#d3b774', '#474747'),
    'Night Blue' : ('#ededed', '#6b9dc2')
}

###########################  T C C  ###################################################
#Icons
light_default_icon = tk.PhotoImage(file='icons/light_default.png')
light_plus_icon = tk.PhotoImage(file='icons/light_plus.png')
dark_icon = tk.PhotoImage(file='icons/dark.png')
red_icon = tk.PhotoImage(file='icons/red.png')
monokai_icon = tk.PhotoImage(file='icons/monokai.png')
night_blue_icon = tk.PhotoImage(file='icons/night_blue.png')

#Add menu TCC na barra
tcc = tk.Menu(main_menu, tearoff=False)

#Add menu Formatação na barra

forma = tk.Menu(main_menu, tearoff=False)

#cascata
main_menu.add_cascade(label='Arquivo', menu=file)
main_menu.add_cascade(label='Editar', menu=edit)
main_menu.add_cascade(label='Visualizar', menu=view)
main_menu.add_cascade(label='Background', menu=color_theme)
main_menu.add_cascade(label='TCC', menu=tcc)
main_menu.add_cascade(label='Formatação', menu=forma)

###################### Toolbar ##########################################
#---------------------&&&&&&&& End Toolbar &&&&&&&&----------------------
tool_bar = ttk.Label(main_application)
tool_bar.pack(side=tk.TOP, fill=tk.X)

#Font Box
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar, width=30, textvariable=font_family, state='readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Times New Roman'))
font_box.grid(row=0, column=0, padx=3)

#size box
size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar, width=7, textvariable= size_var, state='readonly')
font_size['values'] = tuple(range(8,61))
font_size.current(4)
font_size.grid(row=0, column=1, padx=3)

#Botão Negrito
bold_icon = tk.PhotoImage(file='icons/bold.png')
bold_btn = ttk.Button(tool_bar, image=bold_icon)
bold_btn.grid(row=0, column=2, padx=3)

#Botão Italico
italic_icon = tk.PhotoImage(file='icons/italic.png')
italic_btn = ttk.Button(tool_bar, image=italic_icon)
italic_btn.grid(row=0, column=3, padx=3)

#Botão Sublinhado
underline_icon = tk.PhotoImage(file='icons/underline.png')
underline_btn = ttk.Button(tool_bar, image=underline_icon)
underline_btn.grid(row=0, column=4, padx=3)

#Botão Paleta de Cores
font_color_icon = tk.PhotoImage(file='icons/font_color.png')
font_color_btn = ttk.Button(tool_bar, image=font_color_icon)
font_color_btn.grid(row=0, column=5, padx=3)

#alinhamento a esquerda
align_left_icon = tk.PhotoImage(file='icons/align_left.png')
align_left_btn = ttk.Button(tool_bar, image=align_left_icon)
align_left_btn.grid(row=0, column=6, padx=3)

#alinhamento ao centro
align_center_icon = tk.PhotoImage(file='icons/align_center.png')
align_center_btn = ttk.Button(tool_bar, image=align_center_icon)
align_center_btn.grid(row=0, column=7, padx=3)

#alinhamento a direita
align_right_icon = tk.PhotoImage(file='icons/align_right.png')
align_right_btn = ttk.Button(tool_bar, image=align_right_icon)
align_right_btn.grid(row=0, column=8, padx=3)



###################### Text Editor ##########################################
#---------------------&&&&&&&& End Text Editor &&&&&&&&----------------------

#criamos o campo para digitar os textos

text_editor = tk.Text(main_application)
text_editor.config(wrap='word', relief=tk.FLAT)

scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)


### FUNCIONALIDADE DA FONTE E DO TAMANHO ###
current_font_family = 'Times New Roman'
current_font_size = 12


def change_font(event=None):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family, current_font_size))

def change_fontsize(event=None):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font=(current_font_family, current_font_size))    

font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_fontsize)

### FUNCIONALIDADES DOS BOTÕES NEGRIGO/ITALICO/SUBLINHADO ###

###BOLD###
def change_bold():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_font_family, current_font_size, 'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))

bold_btn.configure(command=change_bold)

###ITALIC###
def change_italic():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font=(current_font_family, current_font_size, 'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font=(current_font_family, current_font_size, 'roman'))

italic_btn.configure(command=change_italic)

###SUBLINHADO###
def change_underline():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_family, current_font_size, 'underline'))
    if text_property.actual()['underline'] == 1:
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))

underline_btn.configure(command=change_underline)

####### FONT COLOR FUNCIONALIDADE #######

def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])

font_color_btn.configure(command=change_font_color)

####### ALINHAMENTO FUNCIONALIDADE #######

###ALINHAMENTO A ESQUERDA###
def align_left():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')

align_left_btn.configure(command=align_left)

###ALINHAMENTO AO CENTRO###
def align_center():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')

align_center_btn.configure(command=align_center)

###ALINHAMENTO A Direita###
def align_right():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')

align_right_btn.configure(command=align_right)


############# TAMANHO DA FONTE ##################

text_editor.configure(font=('Times New Roman', '12'))

###################### STATUS BAR ##########################################



#barra de status inferior
status_bar = ttk.Label(main_application, text = 'Status Bar')
status_bar.pack(side=tk.BOTTOM)

###### FUNÇÃO DA STATUS BAR (CONTAGEM DE CARACTERES E LINHAS)######
text_changed = False
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
       text_changed = True
       words = len(text_editor.get(1.0, 'end-1c').split())
       characters = len(text_editor.get(1.0, 'end-1c'))
       status_bar.config(text=f'Caracteres : {characters} Linhas: {words}')
    text_editor.edit_modified(False)
    
text_editor.bind('<<Modified>>', changed)



#---------------------&&&&&&&& End Main Menu &&&&&&&&----------------------


###################### Main Menu Funcionalidades ##########################################

url = ''
def new_file(event=None):
    global url
    url = ''
    text_editor.delete(1.0, tk.END)

#Arquivo SubMenu e adicionar os icones
file.add_command(label='Novo', image=new_icon, compound=tk.LEFT, accelerator='Ctrl+N', command=new_file)
file.add_command(label='Abrir', image=open_icon, compound=tk.LEFT, accelerator='Ctrl+O')
file.add_command(label='Salvar', image=save_icon, compound=tk.LEFT, accelerator='Ctrl+S')
file.add_command(label='Salvar Como', image=save_as_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+S')
file.add_command(label='Sair', image=exit_icon, compound=tk.LEFT, accelerator='Ctrl+Q')

#Editar SubMenu e adicionar os icones
edit.add_command(label='Copiar', image=copy_icon, compound=tk.LEFT, accelerator='Ctrl+C')
edit.add_command(label='Colar', image=paste_icon, compound=tk.LEFT, accelerator='Ctrl+V')
edit.add_command(label='Recortar', image=cut_icon, compound=tk.LEFT, accelerator='Ctrl+X')
edit.add_command(label='Limpar', image=clear_all_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+X')
edit.add_command(label='Procurar', image=find_icon, compound=tk.LEFT, accelerator='Ctrl+F')

#Visualizar SubMenu e adicionar os icones
view.add_checkbutton(label='Tool Bar', image=tool_bar_icon, compound=tk.LEFT)
view.add_checkbutton(label='Status Bar', image=status_bar_icon, compound=tk.LEFT)

#Background Submenu Comando
count = 0
for i in color_dict:
    color_theme.add_radiobutton(label = i, image=color_icons[count], variable=theme_choice, compound=tk.LEFT)
    count += 1


#TCC SubMenu e adicionar os icones
tcc.add_command(label='Capa')
tcc.add_command(label='Lombada')
tcc.add_command(label='Folha de Rosto')
tcc.add_command(label='Introdução')
tcc.add_command(label='Desenvolvimento')
tcc.add_command(label='Conclusão')
tcc.add_command(label='Referências')
tcc.add_command(label='Anexo')
tcc.add_command(label='Glossário')
tcc.add_command(label='Apêndice')
tcc.add_command(label='Agradecimentos')
tcc.add_command(label='Epígrafe')
tcc.add_command(label='Resumo')
tcc.add_command(label='Folha de Aprovação')

#Formatação SubMenu e adicionar os icones
forma.add_command(label='Padrão ABNT')
forma.add_command(label='Padrão XYZ')


#---------------------&&&&&&&& End Main Menu &&&&&&&&----------------------


main_application.config(menu=main_menu)
main_application.mainloop()
