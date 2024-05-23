# trying.py temporary file name
import customtkinter as ctk
import os
import subprocess

# note:
# Please customize the file path according to your system configuration

# class for input window for sub_data
class SubDataInputDialog(ctk.CTkToplevel):
    def __init__(self, parent):
        # object declaration
        # set window size and name
        super().__init__(parent)
        self.title("Sub Data Name")
        self.geometry("300x150")

        # create both Label prompt and button
        self.label = ctk.CTkLabel(self, text="Enter a name for sub_data:")
        self.label.pack(pady=5)

        self.entry = ctk.CTkEntry(self)
        self.entry.pack(pady=5)

        self.ok_button = ctk.CTkButton(self, text="OK", command=self.ok)
        self.ok_button.pack(pady=5)

        self.sub_data = None

    def ok(self):
        self.sub_data = self.entry.get()
        self.destroy()

# class for recoface.py and train.py
class FaceRecognitionUI:
    def __init__(self, root):
        # set window size and name
        self.root = root
        self.root.title("Face Recognition UI")
        self.root.geometry("300x150")

        # button function call
        self.train_button = ctk.CTkButton(self.root, text="Train Face", command=self.train_face)
        self.train_button.pack(pady=10)

        self.recognize_button = ctk.CTkButton(self.root, text="Recognize Face", command=self.recognize_face)
        self.recognize_button.pack(pady=5)

    def train_face(self):
        # run trainface.py and passes the name for sub_data
        sub_data_dialog = SubDataInputDialog(self.root)
        sub_data_dialog.grab_set()  #prevent intercation with parent
        # wait for dialog window
        self.root.wait_window(sub_data_dialog)
        sub_data = sub_data_dialog.sub_data
        if sub_data:
            script_path = "C:\\Lendelcosep\\Codedumps\\repos\\CSC126_FINALS_GROUPTEMP\\trainface.py"
            subprocess.Popen(["python", script_path, sub_data])

    def recognize_face(self):
        # run recoface.py
        script_path = "C:\\Lendelcosep\\Codedumps\\repos\\CSC126_FINALS_GROUPTEMP\\recoface.py"
        subprocess.Popen(["python", script_path])

# main point
if __name__ == "__main__":
    root = ctk.CTk() 
    app = FaceRecognitionUI(root)
    root.mainloop()
