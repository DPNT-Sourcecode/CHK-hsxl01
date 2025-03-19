

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    pricemap = {"E" : 40, "A" : 50, "B" : 30, "C" : 20, "D" : 15}
    skus_count = {"E" : 0, "A" : 0, "B" : 0, "C" : 0, "D" : 0}

    for i in skus:
        if i not in skus_count:
            return -1
        skus_count[i] += 1

    total = 0
    for i in skus_count:
        c = skus_count[i]
        if i == "A" and c >= 5:
            nums = c // 5
            offer_a = nums * 200
            total += offer_a
            c -= (nums * 5)
        if i == "A" and c >= 3:
            nums = c // 3
            offer_a = nums * 130
            total += offer_a
            c -= (nums * 3)
        if i == "B" and c >= 2:
            nums = c // 2
            offer_b = nums * 45
            total += offer_b
            c -= (nums * 2)  
        if i == "E" and c >= 2:
            nums = c // 2
            skus_count["B"] -= nums
            skus_count["B"] = max(skus_count["B"], 0)
            offer_e = nums * 80
            total += offer_e
            c -= (nums * 2) 

        cost = c * pricemap[i]
        total += cost
    
    return total

# print(checkout("EE"))








