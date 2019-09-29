from tkinter import *
import socket
import sys
from protocol2 import Protocol


# _HOST = "<your-ec2-public_ip>"
_HOST = '191.235.89.12'
_PORT = 65439
_REQUEST = "VIDEO"  # "BOOK" || "VIDEO"


class Application(Frame):

    archivo = None

    def descargarArchivo(self):
        print(self.archivo)
        if self.archivo is not None:
            self.ejecutar()

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.grid(column=0, row=2)
        
        self.descargar = Button(self)
        self.descargar["text"] = "Descargar archivo"
        self.descargar["command"] = self.descargarArchivo
        self.descargar.grid(column =1, row =2)

    def traerArchivos(self):
        listbox = Listbox(self)
        for item in ["BOOK", "VIDEO"]:
            listbox.insert(END, item)
        listbox.bind('<<ListboxSelect>>',self.getSelected)
        listbox.grid(column =1, row =1)
    
    def getSelected(self, evt):
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        self.archivo = value
        print(index,value)


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.traerArchivos()
        self.createWidgets()

    def ejecutar(self):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((_HOST, _PORT))

            client = Protocol((_HOST, _PORT), sock, self.archivo)
            client.execute()
        except KeyboardInterrupt:
            print("\n--> [Client End] Caught Keyboard Interrupt.\n--> Exiting\n ")




root = Tk()
root.geometry('400x400')
app = Application(master=root)
app.mainloop()
root.destroy()