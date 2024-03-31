import shutil

class Table:
    def __init__(self, notes):
        self.notes = notes
        self.columns = ['ID', 'Tag', 'Due Date', 'Note Text']
        self.calculate_widths()

    def calculate_widths(self):
        try:
            terminal_width = shutil.get_terminal_size().columns
            max_id_width = max(len(str(note['id'])) for note in self.notes)
            max_tag_width = max(len(str(note['tag'])) for note in self.notes)
            max_due_date_width = 8

            note_text_width = terminal_width - (max_id_width + max_tag_width + max_due_date_width + 5)

            self.column_widths = [max_id_width, max_tag_width, max_due_date_width, note_text_width]
        except:
            self.column_widths = [0, 0, 0, 0]

    def print(self):
        header = '|'.join([title.ljust(width) for title, width in zip(self.columns, self.column_widths)])
        print(header)

        for note in self.notes:
            
            print('-' * len(header))
            id_str = (str(note['id'])).ljust(self.column_widths[0])
            tag_str = (str(note['tag']) if note['tag'] else '').ljust(self.column_widths[1])
            due_date_str = (note['due_date'].strftime('%d.%m.%y') + ' ' if note['due_date'] else ' ' * 9).ljust(self.column_widths[2])
            
            note_text_lines = note['note_text'].split('\n')
            for i, line in enumerate(note_text_lines):
                if i == 0:
                    first_line = (line).ljust(self.column_widths[3]) if len(line) > 20 else line.ljust(self.column_widths[3])
                    print(f"{id_str}|{tag_str}|{due_date_str}|{first_line}")
                else:
                    line_truncated = (line) if len(line) > 20 else line
                    start = ' ' * len(id_str) + '|' + ' ' * len(tag_str) + '|' + ' ' * len(due_date_str)
                    print(start + f"|{line_truncated.ljust(self.column_widths[3])}")