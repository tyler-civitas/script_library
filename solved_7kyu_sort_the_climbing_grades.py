def sort_grades(lst):
    if lst == []:
        return []

    grade_rank = {("V" + str(n)): (n + 3) for n in range(1, 18)}
    grade_rank["VB"] = 1
    grade_rank["V0"] = 2
    grade_rank["V0+"] = 3

    lst.sort(key=(lambda v: grade_rank[v]))

    return lst
