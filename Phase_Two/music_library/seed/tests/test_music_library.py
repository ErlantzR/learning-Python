import unittest

from player.music_library import MusicLibrary, Track


class TestMusicLibrary(unittest.TestCase):
    def test_constructs(self):
        MusicLibrary()

    def test_all_method_exists(self):
        MusicLibrary().all()

    def test_songs_list_empty_when_created(self):
        library = MusicLibrary()
        self.assertEqual(library.all(), [])

    def test_add_method_exists(self):
        MusicLibrary().add("Test song")

    def test_add_a_song_to_list(self):
        library = MusicLibrary()
        library.add("Test song")
        self.assertEqual(library.all(), ["Test song"])
    
    def test_add_a_second_song_to_list(self):
        library = MusicLibrary()
        library.add("Test song")
        library.add("Second test song")
        self.assertEqual(library.all(), ["Test song", "Second test song"])

    def test_remove_method_exists(self):
        MusicLibrary().remove(1)

    def test_remove_a_song(self):
        library = MusicLibrary()
        library.add("Test song")
        library.add("Second test song")
        self.assertEqual(len(library.all()), 2)
        library.remove(1)
        self.assertEqual(len(library.all()), 1)

    def test_remove_an_specific_song(self):
        library = MusicLibrary()
        library.add("Test song")
        library.add("Second test song")
        library.remove(1)
        self.assertEqual(library.all(), ["Test song"])
        library.add("Second test song")
        library.remove(0)
        self.assertEqual(library.all(), ["Second test song"])

    def test_remove_returns_true_when_successfuly_removed(self):
        library = MusicLibrary()
        library.add("Test song")
        self.assertTrue(library.remove(0))

    def test_remove_returns_false_when_index_not_in_list(self):
        library = MusicLibrary()
        library.add("Test song")
        self.assertFalse(library.remove(2))

    def test_adds_tracks(self):
        subject = MusicLibrary()
        subject.add(Track("Moksha", "Caspian", "file.mp3"))
        self.assertEqual(subject.all(), [Track("Moksha", "Caspian", "file.mp3")])

    def test_removes_tracks(self):
        subject = MusicLibrary()
        subject.add(Track("Moksha", "Caspian", "file.mp3"))
        subject.add(Track("Without You", "Dawn Landes", "file.mp3"))
        subject.add(Track("Dry Lips", "Lightspeed Champion", "file.mp3"))
        signal = subject.remove(1)
        self.assertTrue(signal)
        self.assertEqual(
            subject.all(),
            [
                Track("Moksha", "Caspian", "file.mp3"),
                Track("Dry Lips", "Lightspeed Champion", "file.mp3"),
            ],
        )

    def test_lists_tracks(self):
        subject = MusicLibrary()
        subject.add(Track("Moksha", "Caspian", "file.mp3"))
        subject.add(Track("Dry Lips", "Lightspeed Champion", "file.mp3"))
        self.assertEqual(
            subject.all(),
            [
                Track("Moksha", "Caspian", "file.mp3"),
                Track("Dry Lips", "Lightspeed Champion", "file.mp3"),
            ],
        )