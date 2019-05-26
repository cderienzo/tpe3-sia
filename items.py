import pandas

files = ['testdata/armas.tsv', 'testdata/botas.tsv', 'testdata/cascos.tsv', 'testdata/guantes.tsv', 'testdata/pecheras.tsv']                 

def item_value(id, item_id):
    return pandas.read_csv(files[item_id], names=['id', 'strength', 'agility', 'skill', 'resistence', 'life'], skiprows=id+1, nrows=1, delimiter='\t')

def items_count():
    return len(files)        

def item_count():
    with open('testdata/armas.tsv') as item:
        return sum(1 for line in item) - 2