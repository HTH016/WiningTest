def win_corr_code(value):
    return value % 10


def win_corr_cap(value):
    if value % 2 == 0:
        return value
    else:
        return 750


def win_corr_alc(value):
    if value == 20:
        return (0, 100)
    elif value == 21:
        return (0, 8)
    elif value == 22:
        return (8, 11)
    elif value == 23:
        return (11, 13)
    elif value == 24:
        return (13, 15)
    else:
        return (15, 100)


def win_corr_alc_inverse(value):
    if value <= 8:
        return 1
    elif value <= 11:
        return 2
    elif value <= 13:
        return 3
    elif value <= 15:
        return 4
    else:
        return 5


def win_reco_color(user_select, wine_color):
    color_table = [
        [0, 1, 1, 1, 1, 0],
        [0, 5, 1, 3, 1, 0],
        [0, 1, 5, 1, 3, 0],
        [0, 2, 1, 5, 2, 0],
        [0, 5, 1, 1, 1, 0],
        [0, 1, 5, 5, 5, 0],
    ]
    return color_table[user_select][wine_color]


def win_reco_alc(user_select, wine_alc):
    alc_table = [
        [0, 1, 1, 1, 1, 0],
        [0, 5, 5, 3, 2, 1],
        [0, 1, 1, 2, 4, 5],
        [0, 1, 1, 1, 1, 3],
        [0, 3, 3, 3, 3, 3],
        [0, 1, 1, 1, 1, 1],
    ]
    return alc_table[user_select][wine_alc]


def win_reco_taste(user_select, wine_taste):
    taste_table = [
        [0, 1, 2, 3, 2, 1],
        [0, 1, 2, 3, 4, 5],
        [0, 1, 2, 3, 5, 3],
        [0, 1, 3, 5, 3, 1],
        [0, 3, 5, 3, 2, 1],
        [0, 5, 4, 3, 2, 1],
    ]
    return taste_table[user_select][wine_taste]


def win_reco_food(user_select, wine_food):
    food_table = [
        [0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0],
        [0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 3],
    ]
    return food_table[user_select][wine_food]


def sort(a, b):
    l = []
    for i in range(len(a)):
        for j in range(len(a)):
            if sorted(a)[i] == a[j]:
                l.append(b[j])

    result1 = dict.fromkeys(l)  # 리스트 값들을 key 로 변경
    result2 = list(result1)  # list(dict.fromkeys(arr))
    return result2
