"""
File: anagram.py
Name: Ray
----------------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""


FILE = 'dictionary.txt'
EXIT = -1
ANS_LIST=[]

def main():
	"""
	TODO:
	"""

	lib=read_dictionary()

	while True:
		print('Welcome to stanCode "Anagram Generator"(or -1 to quit)')
		word = input('Find anagrams for: ')

		if word == str(EXIT):
			break
		print('Searching...')
		word_list = []
		most = 0

		for ch in word:
			word_list += ch

		for ch in word_list:
			if word_list.count(ch) > most:
				most = word_list.count(ch)

		ans = search(word_list, lib, most)
		print(len(ans), 'anagrams: ', ans)





def search(word_list,lib,most):
	global ANS_LIST

	ANS_LIST = []
	search_helper(word_list,[],len(word_list),lib,most)
	ans = ANS_LIST

	return ans


def search_helper(word_list,chosen,word_len,lib,most):
	global ANS_LIST

	test = ''
	for ch in chosen:
		test += ch
	if test in ANS_LIST:
		return

	elif len(chosen) == word_len and has_prefix2(test,lib) is True:
		print('Found: ',test)
		print('Searching...')
		ANS_LIST += [test]

	elif len(chosen) == word_len:
		return

	elif has_prefix(test,lib) is False:
		return

	else:
		for i in word_list:
			bool = (word_list.count(i)==1 or chosen.count(i)==most)
			if i in chosen and bool:
				pass

			else:
				# choose

				chosen.append(i)
				# explore
				search_helper(word_list, chosen, word_len,lib,most)


				# unchoose
				chosen.pop()



def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""

	list = []
	with open(FILE, 'r') as f:
		for line in f:
			word = line.split('\n')
			list += word
	return list


def has_prefix(sub_s,lib):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
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
