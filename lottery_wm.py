#-*- coding: utf-8 -*- 
# 使用方式 開啟wm 上面擷取下來的csv表單，跟第一份抽出的序號表單，用pipe 執行此py 並且給予 要抽出的獎項數 跟
# 要將抽獎結果 寫入的路徑跟檔名  兩個參數 要先開啟第二階段待抽選的名單
# 指令範例 cat wm_list.csv  0322_google.csv | python lottery_google_form.py 3  ../../1235.csv
# 試算表存檔範例為   
# 職號  分數
# 123   100
# 124    95


import csv,sys,random, codecs, re # 匯入csv 跟 亂數模組random
# 加入re 因為wm的職號 要從()中抽取

wm_result = sys.stdin.readlines() # 接收標準輸入 取得第一階段名單

del wm_result[0]

wm_final = []   #  wm名單
gl_final = []   #  gl名單
all_final = []    #  wm + gl 的名單

for num in wm_result:
    no = str(num).strip("\r\n")   # 將兩階段的名單混合在一起  並接著加入陣列
    no_re = re.findall(r"[r|R]?[0-9]{6,7}", no)  # 使用正規表達式抽取職號
    if no_re == []:
        no_re = ["wm_gl"]      # 加入Google抽獎號碼時，職號與分數的標籤欄位，在regex後會變成[]，無法使用，轉成一區分值
    all_final.append(no_re[0]) # 取得參加wm的人員且及格的名單 + Google表單中獎的人

for p in range(0,len(all_final),1):
    if "wm_gl" in all_final[p]:
        for x in range(0,p,1):
            wm_final.append(all_final[x])
        for y in range(p+1, len(all_final),1):
            gl_final.append(all_final[y])

# 列出兩個陣列相同的地方

wm_set = set(wm_final)
gl_set = set(gl_final)  

wm_candidate = list(wm_set.difference(gl_set)) 
# 利用 set的 difference()  可以從 s1挑出跟s2 重複的資料，並且刪除重複元素，回傳新的s1 並轉為List
# 即為第二階段的抽獎候選名單

same_candidate = list(wm_set.intersection(gl_set))
# 利用 set 的 intersection() 功能 可以列出 兩份名單中有重複的部份

print("第二階段候選抽獎名單" + str(wm_candidate))
print("第二階段候選名單共"+ str(len(wm_candidate)) + "位")
print("第一階段中獎重複參加者" + str(same_candidate))

## 先抽出一個代表序號(index)，再對應到職號的版本 ##
if len(wm_candidate) > 0 and len(wm_candidate) >= int(sys.argv[1]) : # 抽獎候選人要大於0個 且要大於等於被抽出的個數
    prize_num = range(0,len(wm_candidate))  # 用陣列的index下去 抽獎，所以要從0開始，這樣第一個人才能被抽中
    getprize_list = random.sample(prize_num, int(sys.argv[1]))
    print(getprize_list)     #列出得獎代表序號，再對應到職號
    result_save = open(sys.argv[2],"w") # 將抽獎結果存在 命令列參數指定的檔案中
    title = "得獎職號\r\n"   # 組出 抽獎結果的csv
    result_save.write(title)  
    for n in getprize_list:  # 將抽中的得獎代表序號，對應到候選人名單的職號上
        print("得獎職號 : " + wm_candidate[n])
        result_save.write(wm_candidate[n]+"\r\n") 

else:
    print("第二階段無候選人可供抽獎或欲抽出名額大於候選名額")

## 直接抽職號的版本 ##
"""if len(wm_candidate) > 0 and len(wm_candidate) >= int(sys.argv[1]) : # 抽獎候選人要大於0個 且要大於等於被抽出的個數
    getprize_list = random.sample(wm_candidate, int(sys.argv[1])) # 後面命令列參數為要抽幾個得獎者 
    # random.sample的用法 random.sample(樣本群，要抽的個數--接受命令列參數)
    print(getprize_list)  #列出得獎人職號
    result_save = open(sys.argv[2],"w") # 將抽獎結果存在 命令列參數指定的檔案中
    title = "得獎職號\r\n"   # 組出 抽獎結果的csv
    result_save.write(title)  
    for emp_no in getprize_list:
        result_save.write(emp_no+"\r\n") 

else:
    print("第二階段無候選人可供抽獎或欲抽出名額大於候選名額")""" 