import click

from .database import Database
from pymongo import ASCENDING, DESCENDING
from .screen import Table
from .model import Note


collection = None
next_id = None


def initialize_db():
    global collection, next_id
    db = Database()
    collection = db.get_collection()
    next_id = db.next_index


@click.group()
def jot():
    initialize_db()


@jot.command()
@click.option('--tag', default=None, help='Tag for the note')
@click.option('--due', default=None, help='Due date in format dd.mm.yy or delta in days from now on')
@click.argument('note')
def add(tag, due, note):

    note = Note(next_id(), note, tag, due)
    collection.insert_one(note.to_dict())
    click.echo(f"created note {note}")


@jot.command()
@click.option('--sort', default='created_at', help='Sort which column - default is created_at. Possible is id, updated_at, due_date, tag')
@click.option('--direction', default=0, help='Sorting direction - default is descending with 0. Also possible is ascending with 1')
@click.option('--tag', default=None, help='The name of the tag to list notes for')
def list(sort, direction, tag):

    direction_option = 1

    if direction == 0:
        direction_option = DESCENDING
    else:
        direction_option = ASCENDING
        
    find_query = {}
    if tag is not None:
        find_query = {'tag': tag.upper()}

    notes = collection.find(find_query).sort(sort, direction_option)
    notes_for_processing = []
    for note in notes:
        notes_for_processing = notes_for_processing + [note]
    table = Table(notes_for_processing)
    table.print()


def main():
    jot()

if __name__ == "__main__":
    main()
