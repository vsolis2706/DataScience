archive = open('raw-text.txt', "r")
dato = archive.read()
archive.close()

class ProcesarTexto():
     def __init__(self, text):
      formatear_text = text.replace(',', '').replace('.', '').replace('!', '').replace('\n', '')
      self.fmt_text= formatear_text.upper()
      #print(self.fmt_text)
     
     def frecuencias_todo(self):
        palabraLista= self.fmt_text.split(" ")
        #print(palabraLista)
        frecuencias_map = {}
        palabra_set = set(palabraLista)       
        for palabra in palabra_set:
            if palabraLista.count(palabra) == 1:
               frecuencias_map[palabra] = palabraLista.count(palabra)
        return frecuencias_map
   

reto01 = ProcesarTexto(dato)
print(reto01.frecuencias_todo())
