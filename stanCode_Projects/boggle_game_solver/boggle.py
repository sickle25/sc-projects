"""
File: boggle.py
Name: Ray
----------------------------------

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
ANS_LIST = []


def main():

    letter_list = []
    for i in range(4):
        letter_list.append([])
        a_list = []
        print(i+1, end='')
        letter = input(' row of letters:')
        if len(letter)!=7:
            print('Illegal input')
            break
        letter = letter.lower()
        a_list += letter.split()
        letter_list[i]+=a_list




    # letter_list = [['f','y','c','l'],['i','o','m','g'],['o','r','i','l'],['h','j','h','u']]


    ans=find_anagrams(letter_list)
    print('There are',ans,'words in total.')

def read_dictionary():
    list = []
    with open(FILE, 'r') as f:
        for line in f:
            word = line.split('\n')
            list += word
    return list



def find_anagrams(s):
    """
    :param s:
    :return:
    """
    lib = read_dictionary()
    word_list = s
    most = 0
    for i in range(len(word_list)):
        for j in range(len(word_list[i])):
            if word_list.count(word_list[i][j]) > most:
                most = word_list.count(word_list[i][j])

    ans = search(word_list, lib,most)
    return len(ans)



def search(word_list,lib,most):
    global ANS_LIST
    ANS_LIST = []

    for i in range(len(word_list)):
        for j in range(len(word_list[i])):
            search_helper(word_list, [], lib, most, i, j)

    ans = ANS_LIST
    return ans



def search_helper(word_list,chosen,lib,most,old_i,old_j):
    global ANS_LIST

    test = ''
    for ch in chosen:
        test += ch
    if test in ANS_LIST:
        return

    elif len(chosen) >= 4 and has_prefix2(test, lib) is True:
        print('Found: ', test)
        ANS_LIST += [test]

    elif has_prefix(test, lib) is False:
        return

    else:
        for i in range(len(word_list)):
            for j in range(len(word_list[i])):
                bool = (word_list.count(word_list[i][j]) == 1)
                bool2 = ((i - old_i) == 0) and ((j - old_j) == 0)
                if word_list[i][j] in chosen:
                    pass
                elif abs(i-old_i) >1 or abs(j-old_j)>1 or bool2:
                    pass

                else:
                    # choose
                    chosen.append(word_list[i][j])


                    # explore
                    search_helper(word_list, chosen, lib,most,i,j)

                    # unchoose
                    chosen.pop()




def has_prefix(sub_s,lib):
    """
    :param sub_s:
    :return:
    """
    ans = True
    list = lib
    for word in list:

        if sub_s in word[0:(len(sub_s))]:
            ans = True
            break
        else:
            ans = False
    return ans



def has_prefix2(sub_s,lib):
    ans = True
    list = lib
    for word in list:
        if sub_s in word[0:(len(sub_s))]:
            if len(word) > len(sub_s):
                ans = False
                break
            else:
                ans = True
                break
        else:
            ans = False
    return ans



if __name__ == '__main__':
    main()
