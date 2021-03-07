def open_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines
def convert_file_2(lines):
	dic = {}
	for d in lines:
		line = d.split()
		for word in line:
			if word in dic:
				dic[word] += 1
			else:
				dic[word] = 1
	print(dic)
	while True:
		word = input('請輸入要找的人名')
		if word == 'q':
			break
		if word in dic:
			print(word, '出現過的次數', dic[word])
		else:
			print('這個字沒有出現過喔')
	print('謝謝使用收尋')


def main():
	lines = open_file('LINE-Viki.txt')
	lines = convert_file_2(lines)	
	
main()