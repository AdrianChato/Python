#Adrián Solís León 2ºDAM

class Video:
    def __init__(self, titulo_video, duracion, categoria):
        self.titulo_video = titulo_video
        self.duracion = duracion
        self.categoria = categoria

    def mirar_video(self):
        print("Iniciando el video...")
        print(f"El video que estás viendo se titula '{self.titulo_video}' "
              f"de la categoría '{self.categoria}' con una duración de {self.duracion} minutos.")

    def detener_video(self):
        print("Deteniendo el video.")


class Audio:
    def __init__(self, titulo_audio, artista):
        self.titulo_audio = titulo_audio
        self.artista = artista

    def escuchar_audio(self):
        print("Iniciando el audio...")
        print(f"El audio que estás escuchando es '{self.titulo_audio}' "
              f"producido por el artista '{self.artista}'")

    def detener_audio(self):
        print("Deteniendo la reproducción del audio.")


class Media(Video, Audio):
    def __init__(self, titulo, categoria, duracion, artista):
        Video.__init__(self, titulo, duracion, categoria)
        Audio.__init__(self, titulo, artista)



medio_1 = Media("Titulo 1", "infantil", 180, "Artista 1")

medio_1.escuchar_audio()
medio_1.mirar_video()
medio_1.detener_audio()
medio_1.detener_video()
