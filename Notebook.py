from Note import Note


class Notebook:
    FILENAME = "notes.txt"

    def __init__(self):
        self.notes = []
        self.load()

    def load(self):
        try:
            with open(Notebook.FILENAME, 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines), 2):
                    title = lines[i].strip()
                    content = lines[i+1].strip()
                    self.notes.append(Note(title, content))
        except FileNotFoundError:
            pass

    def save(self):
        with open(Notebook.FILENAME, 'w') as file:
            for note in self.notes:
                file.write(f"{note.title}\n{note.content}\n")

    def create(self, title, content):
        note = Note(title, content)
        self.notes.append(note)
        self.save()

    def list_notes(self):
        print("Notes:")
        for index, note in enumerate(self.notes, 1):
            print(f"{index}. {note.title}")

    def get(self, index):
        if 0 < index <= len(self.notes):
            return self.notes[index-1]
        return None

    def edit(self, index, title=None, content=None):
        note = self.get(index)
        if note:
            note.title = title if title else note.title
            note.content = content if content else note.content
            self.save()
            return True
        return False

    def delete(self, index):
        if 0 < index <= len(self.notes):
            del self.notes[index-1]
            self.save()
            return True
        return False
