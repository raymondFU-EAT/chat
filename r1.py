def open_file(filename): #定義一個程式,只能吃檔名
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f: # 把所有資料丟入line變成一條條字串
			lines.append(line.strip()) # 把一條條line的字串刪去分行後，丟入lines列表中
	return lines # 把讀取完的檔案丟出一個結果取名為lines列表

def convert_file(lines):
	new = []
	person = None # 如果命名的person不存在
	for line in lines: 
		if line == 'Allen': # 如果一條條字串中出現Allen的話
			person = 'Allen' # 命名person是Allen
			continue # 如果Allen出現之後，才讓回迴圈繼續
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person: # 如果列表中的person有出現的話
			new.append(person+ ": "+ line) # 把列表人名+': '+人名後面接的內容,丟入新的列表new中
	return new
def write_file(filename, lines): # 寫入程式需要有兩個變數檔名與內容
	with open(filename, 'w')as f: # 打開一個空白要寫入的檔案f 
		for line in lines:  # 把最後完成的列表 lines一條一條讀取後,變成個別資料line
			f.write(line + '\n') # 把讀取的資料line+'\n'換行符號後,寫入空白檔案f中

def main():
	lines = open_file('input.txt')
	lines = convert_file(lines)
	write_file('output.txt',lines)
main()

