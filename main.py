import os
import pathlib
import sqlite3
from dataclasses import dataclass


@dataclass
class Post:
    id: int
    title: str
    description: str


def dict_factory(curs: sqlite3.Cursor, row: tuple) -> dict:
    d = {}
    for idx, col in enumerate(curs.description):
        d[col[0]] = row[idx]
    return d


def get_dict(db: str) -> None:
    connection = sqlite3.connect(db)
    connection.row_factory = dict_factory
    results = connection.execute('select * from posts').fetchall()

    posts = []
    for result in results:
        print(f"{result['id']} {result['title']} {result['description']}")
        post = Post(**result)
        # post.description
        posts.append(post)

    print(posts)
    connection.close()


def get_row(db: str) -> None:
    connection = sqlite3.connect(db)
    results = connection.execute('select * from posts').fetchall()
    for result in results:
        print(f'{result[0]} {result[1]} {result[2]}')
    connection.close()


if __name__ == '__main__':
    db_path = os.path.join(pathlib.Path(__file__).parent.absolute(), 'identifier.sqlite')

    get_dict(db_path)
    get_row(db_path)


# https://www.psycopg.org/docs/extras.html