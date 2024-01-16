import customtkinter as tk
import time 
import pyautogui as pg 
import threading as th 

root = tk.CTk()

fundo = '#11096f'
root.geometry("400x160")
root.title("Python Autoclick")
root.config(background=fundo)
root.resizable(False, False)

#colocar para funcionar     
def contando_pronto():
    zero = 0
    quantidade = int(caixa.get(1.0,tk.END+''))
    while zero < quantidade:
        time.sleep(1)
        pg.click()
        zero = zero +1


def toque_inifinito():
        ze = 0
        time.sleep(2)
        while ze < 1:
            time.sleep(1)
            pg.click()
        

def contado():
    t = th.Thread(target=contando_pronto)
    t.start()



def infinito():
    t = th.Thread(target=toque_inifinito)
    t.start()
    
#customizar




texto_lado_do_mouse = tk.CTkLabel(root, text="número de clicks:", bg_color=fundo )
texto_lado_do_mouse.place(x=20,y=20)

caixa= tk.CTkTextbox(root, height=20, width=70, bg_color=fundo)
caixa.place(x=150,y=20)

botao1 = tk.CTkButton(root,height=30, width=75, text="Iniciar", command=contado, bg_color=fundo)
botao1.place(x=150, y=70)

oii = tk.CTkLabel(root, text="clicks infinitos:", bg_color=fundo)
oii.place(x=20,y=120)

botao2 = tk.CTkButton(root,height=30, width=75, text="iniciar", command=infinito, bg_color=fundo)
botao2.place(x=150, y=120)


root.mainloop()