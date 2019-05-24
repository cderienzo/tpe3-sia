import csv

def items(id, file_id):
    switcher = {
        1: 'testdata/armas.tsv',
        2: 'testdata/botas.tsv',
        3: 'testdata/cascos.tsv',
        4: 'testdata/guantes.tsv',
        5: 'testdata/pecheras.tsv',
    }
    string = switcher.get(file_id)
    with open(string) as tsv:
        csv_reader = csv.reader(tsv, dialect="excel-tab")
        line_count = 0
        for row in csv_reader:
            if line_count-1 == id:
              array = [row[1], row[2], row[3], row[4], row[5]]
            line_count+=1 
              
    return array

