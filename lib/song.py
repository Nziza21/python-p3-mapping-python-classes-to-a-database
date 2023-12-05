import sqlite3

class Song:
    def __init__(self, name, album, song_id=None):
        self.id = song_id  
        self.name = name
        self.album = album

    def save(self):
        with sqlite3.connect('music.db') as conn:
            cursor = conn.cursor()
            if self.id is None:
                cursor.execute("INSERT INTO songs (name, album) VALUES (?, ?)", (self.name, self.album))
                self.id = cursor.lastrowid
            else:
                cursor.execute("UPDATE songs SET name=?, album=? WHERE id=?", (self.name, self.album, self.id))

    @classmethod
    def create_table(cls):
        with sqlite3.connect('music.db') as conn:
            conn.execute('''CREATE TABLE IF NOT EXISTS songs (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            album TEXT
                         )''')

    @classmethod
    def create(cls, name, album):
        song = cls(name, album)
        song.save()
        return song