import pandas

files = ['testdata/armas.tsv', 'testdata/botas.tsv', 'testdata/cascos.tsv', 'testdata/guantes.tsv', 'testdata/pecheras.tsv']                 
item_count_global = 0

def item_value(id, item_id):
    return pandas.read_csv(files[item_id], names=['id', 'strength', 'agility', 'skill', 'resistence', 'life'], skiprows=id+1, nrows=1, delimiter='\t')

def items_count():
    return len(files)        

def item_count():
    global item_count_global
    if (item_count_global == 0):
        with open(files[0]) as item:
                item_count_global = sum(1 for line in item) - 2            
    return item_count_global