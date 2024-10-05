import csv

mydict = {}
with open("plugins/bin/output.csv", mode="r", encoding="utf-8") as inp:
    reader = csv.reader(inp)
    for x in reader:
        x2 = {
            "country": x[1],
            "flag": x[2],
            "brand": x[3],
            "Type": x[4],
            "category": x[5],
            "issuer": x[6],
            "prepaid": True if x[5] == "PREPAID" else False,
        }
        mydict[x[0]] = x2
