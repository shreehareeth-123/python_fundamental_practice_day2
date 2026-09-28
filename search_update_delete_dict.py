prices = {"pen": 10, "book": 50, "bag": 300}
print("Search:", prices["book"])
prices["book"] = 60
print("After update:", prices)
del prices["bag"]
print("After delete:", prices)
