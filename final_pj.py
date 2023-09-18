import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext

def main():
    root = tk.Tk()
    Entry(root).master.title("Essay Assistant")
    ttk.Label(root, text="Essay Assistant",font=("Times New Roman", 17)).grid(column=0, row=0,columnspan=5,pady=3, padx=10)
    ttk.Label(root, text="Enter your essay", font=("Bold", 12)).grid(column=0, row=1,columnspan=5,pady=3, padx=10)

    # Create the Text area.
    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20, font=("Times New Roman", 16))

    # Locate the Text area.
    text_area.grid(column=0, row=2, columnspan=5 , pady=10, padx=10)

    # placing cursor in text area
    text_area.focus()

    # Call content of the windows
    win_content(root,text_area)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()


def win_content(frm_main,text_area):

    # Create the Labels.
    lbl_num_cha = Label(frm_main, text="Number of Characters: ",font=("Bold", 11))
    lbl_num_cha_r = Label(frm_main, width=3 ,font=("Bold", 11))
    lbl_num_wor = Label(frm_main, text="Number of Words: ",font=("Bold", 11))
    lbl_num_wor_r = Label(frm_main, width=3 ,font=("Bold", 11))
    lbl_num_sen = Label(frm_main, text="Number of Sentences: ",font=("Bold", 11))
    lbl_num_sen_r = Label(frm_main, width=3 ,font=("Bold", 11))
    lbl_num_par = Label(frm_main, text="Number of Paragraphs: ",font=("Bold", 11))
    lbl_num_par_r = Label(frm_main, width=3 ,font=("Bold", 11))

    # Locate the Labels.
    lbl_num_cha.grid(row=3, column=1, padx=3, pady= 5)  
    lbl_num_cha_r.grid(row=3, column=2, padx=3, pady=5)   
    lbl_num_wor.grid(row=4, column=1, padx=3, pady=5)    
    lbl_num_wor_r.grid(row=4, column=2, padx=3, pady=5)
    lbl_num_sen.grid(row=3, column=3, padx=3, pady=5)
    lbl_num_sen_r.grid(row=3, column=4, padx=3, pady=5)
    lbl_num_par.grid(row=4, column=3, padx=3, pady=5)
    lbl_num_par_r.grid(row=4, column=4, padx=3, pady=5)

    # Create the buttons.
    btn_check = Button(frm_main, text="Check",font=("Bold", 11))
    btn_clear = Button(frm_main, text=" Clear ",font=("Bold", 11))

    # Locate the buttons.
    btn_check.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    btn_clear.grid(row=4, column=0, padx=10, pady=5, sticky="w")
  
    # This function will be called each time
    # the user presses the "Check" button.
    def calculate():
        btn_clear.focus()
        content = []
        content = text_area.get("1.0",'end-1c')
        # Number of characters
        characters = len(content)
        lbl_num_cha_r.config(text=f"{characters}")
        # Number of words
        words = content.split()
        counter = 0
        while counter < len(words):
            counter+=1
        lbl_num_wor_r.config(text=f"{counter}")
        # Number of sentences
        sentences = content.count(".")
        lbl_num_sen_r.config(text=f"{sentences}")
        # Number of paragraph
        result=content.splitlines()
        paragraph = len(result)-1
        lbl_num_par_r.config(text=f"{paragraph}")

    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        text_area.delete('1.0', END)
        text_area.focus()
        lbl_num_cha_r.config(text="")
        lbl_num_wor_r.config(text="")
        lbl_num_sen_r.config(text="")
        lbl_num_par_r.config(text="")

    # Bind the clear and check functions
    btn_clear.config(command=clear)
    btn_check.config(command=calculate)


if __name__ == "__main__":
    main()
