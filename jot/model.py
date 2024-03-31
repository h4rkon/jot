from datetime import datetime, timedelta

class Note:

    def __init__(self, id, note_text, tag=None, due=None):
        self.id = id
        self.note_text = note_text
        if tag is None:
            self.tag = None
        else:
            self.tag = tag.upper()
        self.due_date = self.parse_due_date(due)
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def parse_due_date(self, due):
        if due is None:
            return None
        if due.isdigit():
            return datetime.now() + timedelta(days=int(due))
        try:
            return datetime.strptime(due, '%d.%m.%y')
        except ValueError:
            raise ValueError('Due date must be in dd.mm.yy format or an integer representing days from today.')

    def update(self, note_text=None, tag=None, due=None):
        if note_text is not None:
            self.note_text = note_text
        if tag is not None:
            self.tag = tag
        if due is not None:
            self.due_date = self.parse_due_date(due)
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
            'id': self.id,
            'note_text': self.note_text,
            'tag': self.tag,
            'due_date': self.due_date,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def __str__(self):
        return (f"ID: {self.id}\n"
                f"Note: {self.note_text}\n"
                f"Tag: {self.tag}\n"
                f"Due Date: {self.due_date.strftime('%d.%m.%Y') if self.due_date else 'None'}\n"
                f"Created At: {self.created_at.strftime('%d.%m.%Y %H:%M')}\n"
                f"Updated At: {self.updated_at.strftime('%d.%m.%Y %H:%M')}")


    @staticmethod
    def from_dict(note_dict):
        id = note_dict.get('id')
        note_text = note_dict.get('note_text')
        tag = note_dict.get('tag')
        # For due_date, ensure it's a datetime object if it's not None
        due = note_dict.get('due_date')
        if due is not None:
            due = due.strftime('%d.%m.%y')
        return Note(id, note_text, tag, due)