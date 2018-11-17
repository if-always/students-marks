import numpy as np
import pandas as pd

###总结
###########################################
#age  性别另行插入
info = [['张三',156307315,'理科'],['李四',156307316,'文科'],['王五',156307317,'理科'],['赵六',156307318,'文科']]

columns = ['姓名','学号','分科']

array_1 = np.array(info)
pd_1 = pd.DataFrame(array_1,columns=columns)
#print(pd_10)

sex = ['女','男','男','女']
array_2 = np.array(sex)
pd_1.insert(3,'性别',array_2)    #插入一列
print(pd_1)

#插入总分
grades = [[156307315,100,100,100],[156307316,99,150,90],[156307317,98,140,80],[156307318,100,160,90]]
columns = ['学号','语文','数学','英语']

array_3 = np.array(grades)
pd_2 = pd.DataFrame(array_3,columns=columns)
#print(pd_11)

total = [300,339,318,350]
array_4 = np.array(total)
pd_2.insert(4,'总分',array_4)
print(pd_2)





pd_1['学号'] = pd_1['学号'].apply(int)  #更改某列的数值类型
pd_2['学号'] = pd_2['学号'].apply(int)  #更改某列的数值类型


pd_3 = pd.merge(left=pd_1,right=pd_2,on='学号')  #两个表格左右合并  以某列形同columns为基准
print(pd_3)
array_5 = np.array(pd_3)
result = np.where(array_5[:,-1] > 311,'合格','不合格')

pd_3.insert(8,'情况',result)
# #pd_12.drop('情况')
print(pd_3)
# #pd_12.to_excel('test.xlsx')
# ###创建数据透视表
means_1 = pd_3['语文'].mean()            #.sum()              #统计语文平均成绩
print(means_1)
means_3 = pd_3.groupby(['性别']).agg({'总分':np.mean})  #统计男女平均总分
print(means_3)
# #类似于groupby  

# pd_14 = pd.pivot_table(pd_12,values=['语文','数学','英语'],index=['分科','性别'],aggfunc=np.mean)
# #print(result)
result_2 = pd_3[(pd_3["分科"] == "文科") & (pd_3["性别"] == '女')]  #找出文科班女所有数据
print(result_2)
result_3 = pd_3[(pd_3['语文']>=100) | (pd_3['英语']>=90)]          #找出语文大于100或者英语大于90的数据
print(result_3)

result_4 = pd_3[(pd_3['性别'] == '女') & (pd_3['总分'] >= 312 )]   #找出女生过线的人
print(result_4)

pd_3['平均分'] = ((pd_3['语文']+pd_3['数学']+pd_3['英语'])/3).apply(int)  #计算平均分
print(pd_3)


def score(grade):
	grade = grade + np.random.randint(0,6)
	return grade

pd_3['附加总分'] = pd_3['总分'].apply(score)    #加上附加分
print(pd_3)

#pd_3.to_excel('case_1.xlsx')

pd_3_sort = pd_3.sort_values("总分",ascending=True)   #按照某一列进行排序
print(pd_3_sort)
