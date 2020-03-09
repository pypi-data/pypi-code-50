"""
Performs operations on taxonomies.
"""
from pathlib import Path
import os, csv, string
import itertools

from peewee import *
from peewee import chunked
from playhouse.db_url import connect

db = SqliteDatabase('../data/test.db')

#db = connect("sqlite:///:memory:")

LIMIT = 1000
SIZE= 10000

class Names(Model):
    tax_id = IntegerField(primary_key=True)
    name = CharField()

    class Meta:
        database = db

    def __str__(self):
        return f"{self.tax_id}:{self.name}"

# Create the indices
idx1 = Names.index(Names.tax_id)
Names.add_index(idx1)

idx2 = Names.index(Names.name)
Names.add_index(idx2)

class Nodes(Model):
    tax_id = IntegerField(primary_key=True)
    parent_id = IntegerField()
    rank = CharField()
    embl_code = CharField()
    division_id = CharField()

    class Meta:
        database = db

    def __str__(self):
        name = Names.get(Names.tax_id==self.tax_id)
        return f"{self.tax_id}:{name.name}:{self.rank}"

db.connect()
db.create_tables([Names, Nodes])


def strip(t):
    return t.strip()

def path(*args):
    return os.path.join(*args)

def parse_names():
    fname = path(".", "..", "data", "names.dmp")
    stream = csv.reader(open(fname, "rt"), delimiter="|")
    stream = map(lambda x: list(map(strip, x)), stream)
    stream = filter(lambda x: x[3] == "scientific name", stream)
    stream = itertools.islice(stream, LIMIT)

    def generate():
        for row in stream:
            entry = dict(tax_id=int(row[0]), name=row[1])
            yield entry

    source = generate()
    print("*** reading names.dmp")
    load(Names, source, size=SIZE)

def parse_nodes():

    fname = path(".", "..", "data", "nodes.dmp")
    stream = csv.reader(open(fname, "rt"), delimiter="|")
    stream = map(lambda x: list(map(strip, x)), stream)
    stream = itertools.islice(stream, LIMIT)

    def generate():
        for row in stream:
            #print (row)
            tax_id, parent_id, = int(row[0]), int(row[1])
            rank, embl_code, division_id = row[2], row[3], row[4]
            entry = dict(tax_id=tax_id, parent_id=parent_id, rank=rank,
                         embl_code=embl_code, division_id=division_id)
            yield entry

    source = generate()

    print("*** reading nodes.dmp")
    load(Nodes, source, size=SIZE)


def load(klass, source, size):
    with db.atomic():
        num = 0
        for step, batch in enumerate(chunked(source, size)):
            num += len(batch)
            print(f"\r*** loading {num:,d} rows", end='')
            klass.insert_many(batch).execute()
    print("")

def build():

    tax_id = 2628082

    node = Names.get(Names.tax_id==tax_id)



    parent = Nodes.get(Nodes.parent_id==node.tax_id)

    print (node)
    print (parent)

def parse_all():

    fname = path(".", "..", "data", "names.dmp")
    stream = csv.reader(open(fname, "rt"), delimiter="|")
    stream = map(lambda x: list(map(strip, x)), stream)
    stream = filter(lambda x: x[3] == "scientific name", stream)
    stream = itertools.islice(stream, LIMIT)

    # Populate taxons by name
    store = {}
    for row in stream:
        tax_id, name = int(row[0]), row[1]
        if tax_id in store:
            print("double taxid", tax_id)
        else:
            store[tax_id] = dict(name=name, children=[])




def delete():
    n = Names.delete().execute()
    m = Nodes.delete().execute()
    print ("Deleted", n, m)


def test():
    count = Names.select().limit(3)
    for c in count:
        print(c.name)


def main():
    #delete()
    parse_all()
    #parse_nodes()
    #test()
    #build()



if __name__ == '__main__':
    main()
