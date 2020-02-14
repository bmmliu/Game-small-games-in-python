"""Final Project"""


def string_reverse(string):
    if len(string) <= 1:
        return string
    return string_reverse(string[1:]) + string[0]


def heng_zhengsub(L, L2):
    Ll = ''.join(L)
    Ll2 = ''.join(L2)

    if Ll in Ll2:
        changdu = len(Ll)
        cha = len(Ll2) - len(Ll)
        i = 0
        while i < (cha + 1):
            if Ll == Ll2[i:(i + changdu)]:

                return i, (i + changdu - 1)

            else:
                i = i + 1
    else:
        pass


def heng_zheng(ci, biao, final_list):
    for elements1 in ci:
        i = 0
        while i < len(biao):
            a = heng_zhengsub(elements1, biao[i])
            if a == None:
                i = i + 1
                pass
            else:
                list2 = []
                start = (i, a[0])
                end = (i, a[1])
                list2.append(start)
                list2.append(end)
                a = ''.join(elements1)
                final_list[a] = list2
                i = i + 1
    return final_list


def heng_daosub(L, L2):
    Ll = ''.join(L)
    Ll2 = ''.join(L2)
    Ll = string_reverse(Ll)

    if Ll in Ll2:
        changdu = len(Ll)
        cha = len(Ll2) - len(Ll)
        i = 0
        while i < (cha + 1):
            if Ll == Ll2[i:(i + changdu)]:

                return i, (i + changdu - 1)

            else:
                i = i + 1
    else:
        pass


def heng_dao(ci, biao, final_list):
    for elements1 in ci:
        i = 0
        while i < len(biao):
            a = heng_daosub(elements1, biao[i])
            if a == None:

                i = i + 1
                pass
            else:
                list2 = []
                start = (i, a[0])
                end = (i, a[1])
                list2.append(end)
                list2.append(start)
                a = ''.join(elements1)
                final_list[a] = list2
                i = i + 1
    return final_list


def shu_dao(ci, biao, final_list):
    for elements1 in ci:
        i = 0
        while i < len(biao):
            a = heng_daosub(elements1, biao[i])
            if a == None:

                i = i + 1
                pass
            else:
                list2 = []
                start = (a[0], i)
                end = (a[1], i)
                list2.append(end)
                list2.append(start)
                a = ''.join(elements1)
                final_list[a] = list2
                i = i + 1
    return final_list


def shu_zheng(ci, biao, final_list):
    for elements1 in ci:
        i = 0
        while i < len(biao):
            a = heng_zhengsub(elements1, biao[i])
            if a == None:
                i = i + 1
                pass
            else:
                list2 = []
                start = (a[0], i)
                end = (a[1], i)
                list2.append(start)
                list2.append(end)
                a = ''.join(elements1)
                final_list[a] = list2
                i = i + 1
    return final_list


def search_row(data, word, hang, lie):
    for i in range(hang):
        for j in range(lie):
            start = (i, j)
            temp_word = ""
            if j + 1 >= len(word):
                for k in range(j, j - len(word), -1):
                    temp_word = temp_word + data[i][k]
                if temp_word == word:
                    end = (i, j - len(word) + 1)
                    return start, end
            temp_word = ""
            if j + len(word) <= lie:
                for k in range(j, j + len(word)):
                    temp_word = temp_word + data[i][k]
                if temp_word == word:
                    end = (i, j + len(word) - 1)
                    return start, end

    return None, None


def search_col(data, word, hang, lie):
    for i in range(hang):
        for j in range(lie):
            start = (i, j)
            temp_word = ""
            if i + 1 >= len(word):
                for k in range(i, i - len(word), -1):
                    temp_word = temp_word + data[k][j]
                if temp_word == word:
                    end = (i - len(word) + 1, j)
                    return start, end

            temp_word = ""
            if i + len(word) <= hang:
                for k in range(i, i + len(word)):
                    temp_word = temp_word + data[k][j]
                if temp_word == word:
                    end = (i + len(word) - 1, j)
                    return start, end

    return None, None


def search_diag_1(data, word, hang, lie):
    for i in range(hang):
        for j in range(lie):
            start = (i, j)
            temp_word = ""
            if i + 1 >= len(word) and j + 1 >= len(word):
                for k in range(0, -len(word), -1):
                    temp_word = temp_word + data[i + k][j + k]
                if temp_word == word:
                    end = (i - len(word) + 1, j - len(word) + 1)
                    return start, end

            temp_word = ""
            if i + len(word) <= hang and j + len(word) <= lie:
                for k in range(0, -len(word), -1):
                    temp_word = temp_word + data[i - k][j - k]
                if temp_word == word:
                    end = (i + len(word) - 1, j + len(word) - 1)
                    return start, end

    return None, None


def search_diag_2(data, word, hang, lie):
    for i in range(hang):
        for j in range(lie):
            start = (i, j)
            temp_word = ""
            if i + 1 >= len(word) and j + len(word) <= lie:
                for k in range(0, -len(word), -1):
                    temp_word = temp_word + data[i + k][j - k]
                if temp_word == word:
                    end = (i - len(word) + 1, j + len(word) - 1)
                    return start, end

            temp_word = ""
            if i + len(word) <= hang and j + 1 >= len(word):
                for k in range(0, -len(word), -1):
                    temp_word = temp_word + data[i - k][j + k]
                if temp_word == word:
                    end = (i + len(word) - 1, j - len(word) + 1)
                    return start, end

    return None, None


def main():
    file1 = input('Enter the name of the file that contains the word search: ')
    with open(file1, 'r') as file:
        lines = file.readlines()
    no1 = lines[0].strip('\n')
    hang1 = no1.split(' ')
    temp = lines[0].strip('\n').split()
    hang = int(temp[0])
    lie = int(temp[1])
    ciorigon = lines[hang + 2:]
    biaoorigon = lines[1:hang + 1]
    biao = []
    ci = []
    biao1 = []

    temp = lines[0].strip('\n').split()

    for elements in biaoorigon:
        new = elements.strip('\n').upper()
        new2 = new.split(' ')
        biao.append(new2)
    for elements in ciorigon:
        new = elements.strip('\n').upper()
        new2 = list(new)
        ci.append(new2)
    final_list = {}
    for i in range(len(biao[0])):
        n = []
        for j in range(len(biao)):
            n.append(biao[j][i])
        biao1.append(n)
    words = []
    for line in lines[hang + 2:]:
        words.append(line.strip().upper())
    words.sort()
    for word in words:
        start, end = search_row(biao, word, hang, lie)
        if start is None and end is None:
            start, end = search_col(biao, word, hang, lie)
        if start is None and end is None:
            start, end = search_diag_1(biao, word, hang, lie)
        if start is None and end is None:
            start, end = search_diag_2(biao, word, hang, lie)
        print(word, end=' ')
        print('starts at', (start[0], start[1]), end=' ')
        print('and ends at', (end[0], end[1]))


main()

# CATDOG starts at (0, 7) and ends at (0, 12)
# HorzOnlyWordSearch.txt
# HorzForwardsOnlyWordSearch.txt
# HorzBackwardsOnlyWordSearch.txt
# VertDownOnlyWordSearch.txt
# RevLeftDiagOnlyWordSearch.txt
# LeftDiagOnlyWordSearch.txt
# RightDiagOnlyWordSearch.txt
# WordSearch1.txt
# RevRightDiagOnlyWordSearch.txt
