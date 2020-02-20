
def get_lib_score(lib, days):
    days_left = days-lib.sign_time
    return lib.score(days_left)

def get_greedy(libs, days):
    libs_left = libs[:]
    days_left = days
    res = []
    while days_left > 0 and len(libs_left)>0:
        max_score = 0
        max_index = 0
        for i in range(len(libs_left)):
            max_score = max(get_lib_score(libs_left[i], days_left), max_score)
            max_index = i
        res.append(libs_left[max_index])
        days_left-=libs_left[max_index].sign_time
        print("max_index", max_index)
        libs_left.pop(max_index)
    return res
