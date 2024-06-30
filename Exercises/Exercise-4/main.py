import glob
import os
import regex as re
import json
import csv

def main():
    cwd = os.getcwd()
    paths=[]
    for name in glob.glob(cwd+'\\**\\*?.json',recursive=True):
        print(name)
        paths.append(name)
    csvs=[re.sub('.json','.csv',path.split('\\')[-1]) for path in paths]
    for i in range(0,len(paths)):
        with open(paths[i]) as f:
            dic=json.load(f)
            dic.pop('geolocation', None)
            fieldnames=dic.keys()
            with open(csvs[i], 'x') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows([dic])
if __name__ == "__main__":
    main()
