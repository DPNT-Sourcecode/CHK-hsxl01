

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    pricemap = {"E" : 40, "A" : 50, "B" : 30, "C" : 20, "D" : 15, "F" : 10}
    skus_count = {"E" : 0, "A" : 0, "B" : 0, "C" : 0, "D" : 0, "F" : 0}

    for i in skus:
        if i not in skus_count:
            return -1
        skus_count[i] += 1

    def offer(c, total, item, num, new_price):
        nums = c // num
        offer_price = nums * new_price
        total += offer_price
        c -= (nums * num)
        return total, c
    
    def get_one_free(c, total, item, free_item, num):
        nums = c // num
        skus_count[free_item] -= nums
        skus_count[free_item] = max(skus_count[free_item], 0)
        offer_price = nums * (pricemap[item] * num)
        total += offer_price
        c -= (nums * num)
        return total, c

    total = 0
    for i in skus_count:
        c = skus_count[i]
        # if i == "A" and c >= 5:
        #     nums = c // 5
        #     offer_a = nums * 200
        #     total += offer_a
        #     c -= (nums * 5)
        if i == "A":
            total, c = offer(c, total, "A", 5, 200)
            total, c = offer(c, total, "A", 3, 130)
        if i == "B":
            total, c = offer(c, total, "B", 2, 45)
        if i == "F":
            total, c = offer(c, total, "F", 3, 20)
        # if i == "A" and c >= 3:
        #     nums = c // 3
        #     offer_a = nums * 130
        #     total += offer_a
        #     c -= (nums * 3)
        # if i == "B" and c >= 2:
        #     nums = c // 2
        #     offer_b = nums * 45
        #     total += offer_b
        #     c -= (nums * 2)  
        if i == "E" and c >= 2:
            nums = c // 2
            skus_count["B"] -= nums
            skus_count["B"] = max(skus_count["B"], 0)
            offer_e = nums * 80
            total += offer_e
            c -= (nums * 2) 
        # if i == "F" and c >= 3:
        #     nums = c // 3
        #     offer_f = nums * 20
        #     total += offer_f 
        #     c -= (nums * 3)    

        cost = c * pricemap[i]
        total += cost
    
    return total

print(checkout("FF"))








