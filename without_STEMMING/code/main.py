# IMPORT ALL FILE
from matplotlib.pyplot import fill
import query_jawaban
import tkinter as tk
from tkinter import *
from tkinter import ttk
import customtkinter

"""# Test"""

# Satu Pertanyaan
# teks_tanya = "siapa yang memindahkan ibukota ke ciguling?"
# print(query_jawaban.jwbjawaban(teks_tanya))

# Fungsi Scroll
class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

# Tema System
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

main_window = customtkinter.CTk()
main_window.geometry("600x520")
main_window.title('QAS Kerajaan Sumedang Larang by Silvia Atika A')

count = 0

def tanya():
    global count
    count = count + 1
    frame_chat_tanya = customtkinter.CTkFrame(frame.scrollable_frame,
                                    width=250
                                    )
    frame_chat_tanya.grid(column=1, row=count)
    label_tanya = customtkinter.CTkLabel(frame_chat_tanya,
                                        text="Pertanyaan \n" + inputQ.get(),
                                        # text_color='#fff',
                                        wraplength=250,
                                        width=250,
                                        anchor="e",
                                        justify=tk.RIGHT)
    label_tanya.grid(column=1, row=count)
    jawab()  

def jawab():
    global count
    count = count + 1
    frame_chat_jawab = customtkinter.CTkFrame(frame.scrollable_frame,
                                    width=250
                                    )                               
    frame_chat_jawab.grid(column=0, row=count)
    label_jawab = customtkinter.CTkLabel(frame_chat_jawab,
                                        text="Jawaban \n" + query_jawaban.jwbjawaban(inputQ.get()),
                                        # text_color='#fff',
                                        wraplength=250,
                                        width=250,
                                        anchor="w",
                                        justify=tk.LEFT)
    label_jawab.grid(column=0, row=count)                                                                         

# Layout
main_window.grid_columnconfigure(0, weight=0)
main_window.grid_rowconfigure(0, weight=1)

# Chat
frame = ScrollableFrame(main_window)
frame.grid(row=0, sticky="nswe", columnspan=2, padx=20, pady=20)

# Field Pertanyaan
frame_bottom = customtkinter.CTkFrame(master=main_window, height=50, corner_radius=0)
frame_bottom.grid(row=1, sticky="nswe", padx=20, pady=20)

inputQ = customtkinter.CTkEntry(master=frame_bottom,
                                width=300,
                                placeholder_text="Masukkan pertanyaan...")
inputQ.grid(row=1, column=0, pady=20, padx=20, sticky="we")

myButton = customtkinter.CTkButton(master=frame_bottom,
                                    text="Tanya",
                                    border_width=2,
                                    fg_color=None,
                                    command=tanya)
myButton.grid(row=1, column=1, pady=20, padx=20, sticky="we")

main_window.mainloop()


# df_pertanyaan = pd.read_csv('\import\Pertanyaan_Fix.csv')
# df_pertanyaan['pertanyaan test'].head()

# hasiljwb = []
# for tanya in df_pertanyaan['pertanyaan test']:
#   menjwb = hasil_jawaban(tanya)
#   hasiljwb.append(menjwb)

# df_pertanyaan['hasil jawaban'] = hasiljwb

# df_pertanyaan.head()

# df_pertanyaan.to_csv('hasil.csv')


