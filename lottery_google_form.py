#-*- coding: utf-8 -*- 
# 使用方式 開啟從Google表單擷取下來的結果 執行此py檔案，給予兩個參數 第一個要抽出幾份獎品的數字
# 第二個要將結果存為XXXXX.csv
# 指令範例 cat lottery_list.csv | python lottery_google_form.py 3  246.csv
# Google試算表存檔範例為   
# 職號  分數
# 123   100
# 124    95

import csv,sys,random # 匯入csv 跟 亂數模組random

get_list = sys.stdin.readlines() # 接收標準輸入 取得抽獎名單

gln = []         # 用來儲存排除 重複填寫問卷且分數相同的 新陣列 (其中資料會是唯一)

del get_list[0] # 移除掉 第一列的標籤名稱列

for x_line in get_list:
    row_data = str(x_line).strip("\r\n")   # 將職號與分數對應 去除掉換行符號，作為後續計算次數的依據
    gln.append(row_data)

gln_n = set(gln)    # set用法為 去除掉List中的重複元素，並重新組成一個集合

random_list = []    # 儲存可被抽獎的職號用的陣列

for data in gln_n:
    times = str(gln_n).count(data)
    if times == 1 and data.split(",")[1] == "100":
        random_list.append(data.split(",")[0])

print(random_list)   # 列出得獎人職號
result_list = random.sample(random_list, int(sys.argv[1])) # 後面命令列參數為要抽幾個得獎者 
# random.sample的用法 random.sample(樣本群，要抽的個數--接受命令列參數)
print(result_list)   # 抽出得獎人職號


result_save = open(sys.argv[2],"w") # 將抽獎結果存在 命令列參數指定的檔案中

title = "得獎職號\r\n"   # 組出 抽獎結果的csv
result_save.write(title)  

for emp_no in result_list:
    result_save.write(emp_no+"\r\n")   

