def reader(filename):
    f = open(filename, "r")
    res = dict()
    l1 = f.readline().split()
    res["total_books"] = int(l1[0])
    res["num_lib"] = int(l1[1])
    res["scanning_time"] = int(l1[2])
    res["book_scores"] = list(map(int,f.readline().split()))
    res["libs"] = [0] * res["num_lib"]
    for i in range(res["num_lib"]):
        res["libs"][i] = dict()
        next_line = list(map(int,f.readline().split()))
        res["libs"][i]["num_books"] = next_line[0]
        res["libs"][i]["signup_time"] = next_line[1]
        res["libs"][i]["ship_rate"] = next_line[2]
        res["libs"][i]["books_held"] = list(map(int, f.readline().split()))
    f.close()
    return res
