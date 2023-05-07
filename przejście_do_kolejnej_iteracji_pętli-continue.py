# petla nieskończona ponieważ index += 1 jest za pętla coninue, nie dodaje się

# index = 0
#
# while index < 5:
#     print(index)
#     if index == 2:
#         continue
#     print("Po if")
#     index = index + 1



# przeniesienie index += 1 przed pętle continue
index = 0

while index < 5:
    print(index)
    index = index + 1
    if index == 2:
        continue
    print("Po if")
