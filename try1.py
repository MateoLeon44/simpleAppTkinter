from tkinter import *

class Application(Frame):

    archivo = None

    def descargarArchivo(self):
        if self.archivo is not None:
            print(self.archivo)
            return

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.grid(column=0, row=2)
        
        #self.desc_libro = Button(self)
        #self.desc_libro["text"] = "Descargar libro"
        #self.desc_libro["command"] = self.descargarLibro
        #self.desc_libro.grid(column =1, row =2)

        self.descargar = Button(self)
        self.descargar["text"] = "Descargar archivo"
        self.descargar["command"] = self.descargarArchivo
        self.descargar.grid(column =1, row =2)

    def traerArchivos(self):
        listbox = Listbox(self)
        for item in ["one", "two", "three", "four"]:
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

root = Tk()
root.geometry('400x400')
app = Application(master=root)
app.mainloop()
root.destroy()