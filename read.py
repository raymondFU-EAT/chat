count = 0
data = []
with open("reviews.txt", "r") as f: 
	for line in f:
		data.append(line)
		count += 1
		if count % 100000 == 0:
			print(len(data))
print("收尋資料總共為", len(data), "筆資料")
number = 0
for count_1 in data:
	number = number + len(count_1)
print("每行資料平均為", number/len(data), "個字")

new = []
for d in data:
	if len(d) < 100:
		new.append(data)
print("總共有", len(new), "筆資料長度小於100")

good = [] # 設一個資料夾為good
for e in data: # 從data中找出我要的資料e
	if "good" in e: # 如果我找到的資料中有字串good
		good.append(data) # 把找到的字串放入設的資料夾good中
print("總共有",len(good),"好的留言")

good = [e for e in data if "good" in e] # 設立一個Good的資料夾,把有good留言的各條資料從data中找出
print(len(good))
new = [d for d in data if len(d) < 100] # 設立一個New的資料夾,把所有留言少於100字的資料找出來
print(len(new))


wc = {} # 設立一個字典w
for d in data: # 把整筆資料data放入字列表d中(變成一筆一筆留言)
	words = d.split(' ') # 把留言之間的空格清除後,放入新的列表words中(變成全部都是獨立的文字)
	for word in words:  # 依序把留言中的所有文字,一個一個字放入word列表中
		if word in wc: # 如果在字典中提到其中一個字
			wc[word] += 1 # 那就計算提到的字
		else:             # 如果該字沒有在字典中
			wc[word] = 1  # 那就新增提到的字,並且提到的數量計為1
for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

while True:
	word = input('請問你要查甚麼字')
	if word =='q':
		break
	if word in wc:
		print(word, '出現過的次數', wc[word])
	else:
		print('這個字沒有出現過喔')
print('謝謝使用查詢功能')




