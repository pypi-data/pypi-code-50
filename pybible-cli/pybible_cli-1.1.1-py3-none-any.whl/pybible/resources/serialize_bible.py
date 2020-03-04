from pybible.classes.bible_without_apocrypha import BibleWithoutApocrypha
from pybible.classes.book import Book
from pybible.classes.chapter import Chapter
from pybible.classes.verse import Verse
from re import match
import pickle

with open("bibles/kj.txt", "r", encoding="utf-8") as fp:
    books = list()
    chapters = list()
    verses = list()
    for line in fp:
        if match("^\\d+:\\d+.*", line):
            split_pos = line.find(" ")
            chapter, verse = line[:split_pos].split(":")
            text = line[split_pos:].strip()
            if chapter_count != chapter:
                chapters.append(Chapter(int(chapter_count), tuple(verses)))
                chapter_count = chapter
                verses = []
            verses.append(Verse(text, int(verse)))
        else:
            if chapters or "Genesis" not in line:
                chapters.append(Chapter(int(chapter_count), tuple(verses)))
                books.append(Book(book_title, book_full_title, author, tuple(chapters)))
            chapter_count = "1"
            chapters = []
            verses = []
            book_title, book_full_title, author = line.split("/")

    chapters.append(Chapter(int(chapter_count), tuple(verses)))
    books.append(Book(book_title, book_full_title, author, tuple(chapters)))

    kj = BibleWithoutApocrypha("King James Bible", "English", books)

    bible_file = open("bibles_serialized/kj", "w+b")

    pickle.dump(kj, bible_file)
    bible_file.close()

    kj_file = open("bibles_serialized/kj", "rb")
    kj = pickle.load(kj_file)
    kj_file.close()

    print(kj)





