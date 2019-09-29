from tkinter import *
from tkinter import messagebox
import socket
import sys
from protocol2 import Protocol


# _HOST = "<your-ec2-public_ip>"
_HOST = '191.238.209.152'
_PORT = 3333
_REQUEST = "VIDEO"  # "BOOK" || "VIDEO"


class Application(Frame):

    archivo = None
    client = None


    def descargarArchivo(self):
        print(self.archivo)
        if self.archivo is not None:
            self.ejecutar()

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.grid(column=0, row=1)
        
        self.descargar = Button(self)
        self.descargar["text"] = "Descargar archivo"
        self.descargar["command"] = self.descargarArchivo
        self.descargar.grid(column =1, row =1)

    def traerArchivos(self):
        listbox = Listbox(self, width=40, height=10)
        self.client._read()
        archivos = self.client.darFiles()
        for value in archivos.values():
            listbox.insert(END,value['name'])
        listbox.bind('<<ListboxSelect>>',self.getSelected)
        listbox.grid(column =0, row =0)
    
    def getSelected(self, evt):
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        if value == 'Closer - Lemaitre':
            value = 'VIDEO'
            self.client.req = 'VIDEO'
        else:
            value = 'BOOK'
            self.client.req = 'BOOK'
        self.archivo = value
        print(index,value)


    def __init__(self, master=None):
        Frame.__init__(self, master)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((_HOST, _PORT))
            messagebox.showinfo("Conexión al servidor", "Se estableció la conexión con el servidor" + _HOST)
            self.client = Protocol((_HOST, _PORT), sock, 'VIDEO')
            self.pack()
            self.traerArchivos()
            self.createWidgets()
        except:
            messagebox.showinfo("Error", "No se pudo establecer conexión con el servidor " + _HOST)
            root.destroy()
        

    def ejecutar(self):
        try:
            print(self.client.req)
            self.client.execute()
            messagebox.showinfo("Mensaje de comprobación", self.client.imprimirRespuesta() + ". El tiempo desde conexión hasta el final de la transferencia fue de: " + self.client.darTiempo() + " segundos")
        except KeyboardInterrupt:
            print("\n--> [Client End] Caught Keyboard Interrupt.\n--> Exiting\n ")




root = Tk()
root.geometry('400x400')
app = Application(master=root)
app.mainloop()
root.destroy()