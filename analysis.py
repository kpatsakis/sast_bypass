import pandas as pd    
jsonObj = pd.read_json(path_or_buf="newdataset_alessandro.jsonl", lines=True)
first_element = jsonObj[0]
print("First element:", first_element)