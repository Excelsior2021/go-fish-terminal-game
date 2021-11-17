import json

def record(player_pairs, comp_pairs, first_record):
    '''Records game stats externally in JSON format.'''
    try:
        filename = 'record.json'
        with open(filename) as f:
            record = json.load(f)
    except FileNotFoundError:
        filename = 'record.json'
        with open(filename, 'w') as f:
            json.dump(first_record, f)
    else:
        if len(player_pairs) > len(comp_pairs):
            record["Wins"]+=1
        elif len(comp_pairs) > len(player_pairs):
            record["Loses"]+=1
        else:
            record["Draws"]+=1
        filename = 'record.json'
        with open(filename, 'w') as f:
            json.dump(record, f)