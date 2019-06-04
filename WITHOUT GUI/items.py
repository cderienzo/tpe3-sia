import pandas

files = ['../fulldata/armas.tsv', '../fulldata/botas.tsv', '../fulldata/cascos.tsv', '../fulldata/guantes.tsv', '../fulldata/pecheras.tsv']                 
item_count_global = 0

data = [pandas.read_csv(x, sep='\t', header=0) for x in files]

def item_value(id, item_id):
    return data[item_id].iloc[id]

def items_count():
    return len(files)        

def item_count():
    global item_count_global
    if (item_count_global == 0):
        with open(files[0]) as item:
                item_count_global = sum(1 for line in item) - 2            
    return item_count_global