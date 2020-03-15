reference = {}
sources = {}

# SST
x = {}
x['name'] = 'sst'
x['url'] = 'https://nlp.stanford.edu/sentiment/trainDevTestTrees_PTB.zip'
x['unpack'] = 'unzip trainDevTestTrees_PTB.zip -d {tmp}'
x['cleanup'] = 'rm trainDevTestTrees_PTB.zip'
x['splits'] = [
    {'name': 'dev', 'path': 'trees/dev.txt'},
    {'name': 'test', 'path': 'trees/test.txt'},
    {'name': 'train', 'path': 'trees/train.txt'}
]
sources[x['name']] = x

reference['sources'] = sources
