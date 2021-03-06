def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert_file(lines):
	allen_count_number = 0
	allen_count_sticker = 0
	allen_count_image = 0
	viki_count_number = 0
	viki_count_sticker = 0
	viki_count_image = 0
	for line in lines:
		s = line.split( )
		time = s[0]
		name = s[1]
		if name =='Allen':
			if s[2] == '貼圖':
				allen_count_sticker += 1
			elif s[2] == '圖片':
				allen_count_image += 1
			else:
				for m in s[2:]:
					allen_count_number += len(m)	
		if name =='Viki':
			if s[2] == '貼圖':
				viki_count_sticker += 1
			elif s[2] == '圖片':
				viki_count_image += 1
			else:
				for m in s[2:]:
					viki_count_number += len(m)

	print('Allen說了', allen_count_number, '個字')
	print('Allen傳了',allen_count_sticker, '張貼圖',allen_count_image, '張圖片')
	print('Viki說了', viki_count_number, '個字')
	print('Viki傳了',viki_count_sticker, '張貼圖',viki_count_image, '張圖片')
		
def write_file(filename, lines):
	with open(filename, 'w')as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert_file(lines)
	# write_file('output.txt',lines)
main()

