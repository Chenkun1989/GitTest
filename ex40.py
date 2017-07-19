class Song(object):
	"""docstring for Song"""
	def __init__(self, lyrics):
		super(Song, self).__init__()
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

lyrics = ["happy birthday to you", 
		  "I don't want to get sued", 
   	      "So I'll stop right there"]

happy_bday = Song(lyrics)

happy_bday.sing_me_a_song()
		