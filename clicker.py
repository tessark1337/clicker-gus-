
import tkinter as tk
from tkinter.messagebox import showinfo

# переменные

wallet = 10
multiplier = 1
profit = 1
cost = 100

# вспомогательные функции
def round2(n):
    return round(n, 2)

# основные функции
def click():
    global wallet
    global multiplier
    wallet += profit * multiplier
    label_counter['text'] = f'Счётчик гусей\n {round2(wallet)} GusCoins'

def upgrade():
    global multiplier
    global cost
    global wallet
    if wallet >= cost:
       multiplier += 0.05
       wallet -= cost
       cost += 75
       label_counter['text'] = f'Счётчик гусей\n {round2(wallet)} GusCoins'
       label_multiplier['text'] = f'Текущий множитель {round2(multiplier)}'
       label_cost['text'] = f'Стоимость {cost} GusCoins'
    else:
         showinfo(title='Ошибка', message='Недостаточно средств.')
    if multiplier >= 10:
        multiplier += 0.05
        cost += 25
        label_counter['text'] = f'Счётчик гусей\n {round2(wallet)} GusCoins'
        label_multiplier['text'] = f'Текущий множитель {round2(multiplier)}'
        label_cost['text'] = f'Стоимость {cost} GusCoins'

window = tk.Tk()
window.geometry(f'960x660+480+160')
window.title('Gus Combat')
window['bg'] = '#e5d753'
window.maxsize(1080, 720)
window.iconphoto(False, tk.PhotoImage(file='image_gus'))

label = tk.Label(window, text='Gus Combat', font=
                         ('Ink Journal', 64), bg='#e5d753', padx=5, pady=2)

label_counter = tk.Label(window, text=f'Счётчик гусей\n {round2(wallet)} GusCoins', font=('Ink Free', 24), bg='#e5d753', padx=5, pady=2)
label_multiplier = tk.Label(window, text=f'Текущий множитель {round2(multiplier)}', font=('Ink Free', 24), bg='#e5d753', padx=5, pady=2)
label_cost = tk.Label(window, text=f'Стоимость {cost} GusCoins', font=('Ink Free', 24), bg='#e5d753', padx=5, pady=2)

b_click = tk.Button(window, text=f'КЛИК', command=click, font=('Terminal', 16), bg='red', padx=24, pady=8)
b_upgrade = tk.Button(window, text='Прокачка', command=upgrade, font=('Terminal', 24), bg='green', padx=6, pady=12)
b_settings = None
b_exit = tk.Button(window, text='Выход', command=exit, font=('Terminal', 16), fg='white', bg='black', padx=48, pady=16)

label.pack()

label_counter.pack()  # b1
label_multiplier.pack(anchor='w', padx=12, pady=100) # b2
label_cost.place(x=10, y=360)

b_click.place(x=425, y=210)
b_upgrade.place(x=70, y=420)
b_exit.place(x=412, y=560)




tk.mainloop()