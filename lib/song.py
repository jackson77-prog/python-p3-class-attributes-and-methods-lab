class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment count and add song to count
        self.add_song_to_count()

        # Add genre to genres list and update genre count
        self.add_to_genres()

        # Add artist to artists list and update artist count
        self.add_to_artists()

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    def add_to_genres(self):
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

        if self.genre not in Song.genre_count:
            Song.genre_count[self.genre] = 1
        else:
            Song.genre_count[self.genre] += 1

    def add_to_artists(self):
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

        if self.artist not in Song.artist_count:
            Song.artist_count[self.artist] = 1
        else:
            Song.artist_count[self.artist] += 1

    @classmethod
    def add_to_genre_count(cls):
        genre_count = {}
        for genre in cls.genres:
            genre_count[genre] = cls.genre_count.get(genre, 0)
        cls.genre_count = genre_count

    @classmethod
    def add_to_artist_count(cls):
        artist_count = {}
        for artist in cls.artists:
            artist_count[artist] = cls.artist_count.get(artist, 0)
        cls.artist_count = artist_count
