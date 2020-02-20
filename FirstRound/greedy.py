from dataHandler import libs_to_writer, writer
from scorer import score_libs

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
        libs_left.pop(max_index)
    return res

def swap_books_greedily(libs_sol, all_libs, days, all_books, problem):
    import random
    data = libs_to_writer(libs_sol, days)
    max_score = score_libs(data, all_books)
    print("score at beginning is", max_score)
    all_libs = set(all_libs)
    while True:
        trial_sol = libs_sol.copy()
        for i in range(random.randint(0, 3)):
            if len(trial_sol)>1:
                random_id = random.randint(0, len(trial_sol)-1)
                trial_sol.pop(random_id)
        for i in range(random.randint(0, 3)):
            #lib_possible = all_libs - set(trial_sol)
            # lib_possible = all_libs.copy()
            # for lib in trial_sol:
            #     lib_possible.remove(lib)
            rand_id = random.randint(0, len(trial_sol)-1)
            rand_lib = random.sample(all_libs, 1)
            while rand_lib in trial_sol:
                rand_lib = random.sample(all_libs, 1)
            trial_sol.insert(rand_id, rand_lib)
        print((trial_sol[0]))
        data = libs_to_writer(trial_sol, days)
        cur_score = score_libs(data, all_books)
        if cur_score > max_score:
            max_score = cur_score
            libs_sol = trial_sol.copy()
            data = libs_to_writer(libs_sol, days)
            writer(data, "greedy_ans_" + str(problem) + ".txt")
            print("max score is now", max_score)
