import pygame
class MusicPlayer:
    def __init__(self, playlist):
        pygame.mixer.init()
        self.playlist = playlist
        self.current_track = 0
        self.is_playing = False
    def play(self):
        pygame.mixer.music.load(self.playlist[self.current_track])
        pygame.mixer.music.play()
        self.is_playing = True
    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False
    def next_track(self):
        self.current_track = (self.current_track + 1) % len(self.playlist)
        self.play()
    def previous_track(self):
        self.current_track = (self.current_track - 1) % len(self.playlist)
        self.play()
