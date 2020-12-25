from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter.filedialog import asksaveasfile,askopenfile

class text(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("text editor")
        self.master.geometry("1000x500")
        
        self.grid()
        self.menubar=Menu(self)
        self.save_file_id =""
        self.menubar.add_command(label="new", command=self.New_file)
        self.menubar.add_command(label="open", command=self.open)
        self.menubar.add_command(label="save", command=self.save)
        self.menubar.add_command(label="save as", command=self.saveas)

        self.master.config(menu=self.menubar)
        self.menubar.configure(bg="#224a8a")

        self.scrollbar = Scrollbar(self)
        self.scrollbar.pack( side = RIGHT, fill = Y )
        
        self.t=Text(self,yscrollcommand = self.scrollbar.set,width=215,height=50,bg="black",fg="white",font="Lucida 10")
        self.t.pack(side = LEFT, fill = BOTH )
        self.scrollbar.config( command = self.t.yview )
    
    def save(self):
        if self.save_file_id =="":
            self.saveas()
        else:
            self.file=open(self.save_file_id,"w")
            self.text2save = str(self.t.get(1.0, END))
            self.file.write(self.text2save)
            self.file.close()
    
    def saveas(self):
        self.files = [('All Files', '*.*'),  
             ('Python Files', '*.py'), 
             ('Text Document', '*.txt')] 
        self.file = asksaveasfile(filetypes = self.files, defaultextension = self.files)
        self.text2save = str(self.t.get(1.0, END))
        self.file.write(self.text2save)
        self.save_file_id =self.file.name
        self.file.close()
        
    def open(self): 
        self.file = askopenfile(mode ='r', filetypes =[('Text Files', '*.txt'),('Python Files', '*.py')]) 
        if self.file is not None: 
            self.content = self.file.read()
            self.t.insert(END,self.content)
            self.save_file_id=self.file.name
        
    def New_file(self):
	    self.t.delete(1.0, END)
	    self.save_file_id = ""
    
    

        

def main():
    text().mainloop()

main()
