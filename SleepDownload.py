"""Don't forget to Click to Download the Chosen GAME Before Carrying Out this Information"""

# Step 1: Import libraries

import os
import tkinter as tk
from tkinter import messagebox
import time
import threading


# Step 2: ask the User and EXPLAIN how long they want to turn off the computer.

tempo = float(input('What is the time allocated in hours to turn off your computer? (EXAMPLE: 2.5 = 2 AND A HALF HOURS): '))
tempo = tempo * 3600
time.sleep(tempo)

# Step 3: Create a class to turn off by defining a function.

class DesligarComputadorApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Turn Off')
        
        self.label = tk.Label(root, text="Do You Really Want to Turn Off Your Computer?")
        self.label.pack(pady=10)

        self.botao_sim = tk.Button(root, text="Sim", command=self.desligar_agora)
        self.botao_sim.pack(pady=5)

        self.botao_nao = tk.Button(root, text="Não", command=self.cancelar_desligamento)
        self.botao_nao.pack(pady=5)
        
        # Starting a thread to monitor time and shut down the computer after 5 minutes of no response
        self.thread_tempo = threading.Thread(target=self.monitorar_tempo)
        self.thread_tempo.start()
        
    def desligar_agora(self):
        messagebox.showinfo('Turning off', 'Turning off..')
        os.system('shutdown /s /t 1')
        self.root.destroy()  # Close the window after turning off the computer
        
    def cancelar_desligamento(self):
        messagebox.showinfo('Turn off', 'Shutdown cancelled.')
        self.root.destroy()  # Closing the window when clicking "No"

        
    def monitorar_tempo(self):
        # Wait 5 minutes (300 seconds) before turning off the computer automatically
        time.sleep(420)
        messagebox.showinfo('Turn off Computer', 'Time expired. The computer will shut down.')
        os.system("shutdown /s /t 1")
        self.root.destroy()  # Close the window after turning off the computer

if __name__ == "__main__":
    root = tk.Tk()
    app = DesligarComputadorApp(root)
    root.mainloop()
