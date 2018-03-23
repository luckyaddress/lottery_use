#-*- coding: utf-8 -*- 
import csv,sys,random, codecs, re # 匯入csv 跟 亂數模組random
# 加入re 因為wm的職號 要從()中抽取

wm_result = sys.stdin.readlines() # 接收標準輸入 取得第一階段名單

del wm_result[0]

wm_final = []

for num in wm_result:
    no = str(num).strip("\r\n")   # 將兩階段的名單混合在一起  並接著加入陣列
    no_re = re.findall(r"\([a-z0-9]\)", no)
    wm_final.append(no_re)

print(wm_final)
    
"""wm_final_n = set(wm_final)        # 第二階段中如果有分數跟職號完全相同的，用set將之去除

wm_list = []

for wm_data in wm_final_n:
    times = str(wm_final_n).count(wm_data.split(",")[0])   # 每個人在第二階段的職號也能出現一次
    if times == 1 and len(wm_data.split(",")) == 2 :       # 只去取第二階段有來考試的人並且第一階段沒中獎的人
        wm_list.append(wm_data.split(","))                 # (跟上方職號一次取交集) 即可去除掉第一階段中獎還來考試的
    

wm_list_100 = []            # 接著處理過濾掉 沒有考100滿分的人

for x in wm_list:
    if x[1] == "100":
        wm_list_100.append(x[0])  # 取得第一階段沒抽中 第二階段有來考 並只紀錄一次 考100的職號

print(wm_list_100)

getprize_list = random.sample(wm_list_100, int(sys.argv[1])) # 後面命令列參數為要抽幾個得獎者 
# random.sample的用法 random.sample(樣本群，要抽的個數--接受命令列參數)

print(getprize_list)  #列出得獎人職號


result_save = open(sys.argv[2],"w") # 將抽獎結果存在 命令列參數指定的檔案中

title = "得獎職號\r\n"   # 組出 抽獎結果的csv
result_save.write(title)  

for emp_no in getprize_list:
    result_save.write(emp_no+"\r\n")   """

        
