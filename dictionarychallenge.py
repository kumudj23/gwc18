dictA = {
  "first" : 23,
  "third" : 12,
  "fourth" : 22
}

dictB = {
    "first" : 2,
    "second" : 30,
    "third" : 10
}

for key, value in dictB.items():
    if key in dictA:
        dictA[key] += dictB[key]
    else:
        dictA[key] = dictB[key]

print(dictA)
