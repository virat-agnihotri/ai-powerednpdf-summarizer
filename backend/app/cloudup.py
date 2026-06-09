import os 
from tkinter import Tk,filedialog

def open_file_explorer():
    root=Tk()
    root.withdraw()
    root.attributes('-topmost',True)
    selected_file_path=filedialog.askopenfilename(title="Select your PDF to upload to the clout",
                                                  filetypes=[("PDF files","*.pdf")])
    if selected_file_path:
        print(f"Success! You selected:{selected_file_path}")
        print(f"File Name: {os.path.basename(selected_file_path)}")
        return selected_file_path
    else:
        print("User cancelled or closed the file explorer.")
        return None
pdf_to_upload=open_file_explorer()