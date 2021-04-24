import mp3play
filename = r'C:\Users\USER\Desktop\CursoDePython\ModulosEBibliotecas\plausos.mp3'
clip = mp3play.load(filename)
clip.play()