import random
import numpy as np
import pandas as pd

origin_datas = pd.read_csv('origin_grades.csv',encoding="gb2312" )


#print(len(origin_datas))
#print(len(origin_datas["身份证"].unique()))  #以身份证来看  查看是否右重复项

drop_datas = origin_datas.drop_duplicates(subset="身份证",keep='first') # 根据身份证一列去重  subset = 某一列 keep=‘first’ 保留重复项的第一个   重置索引
#print(drop_datas)
#print(origin_datas)


#>>>>>>>>>>>>>增加一列 文理分科
test_list = ["文科","理科"]
class_datas = []
for i in range(27):

	class_data = random.sample(test_list,1)
	class_datas.extend(class_data)


array_class = np.array(class_datas)


new_datas = drop_datas.copy()  #在原表上新添加一列的话  会报错  所以我们建立一个副本

new_datas["分科"] = array_class
#new_datas.loc["分科"] = new_datas.columns.insert(8,"分科",array_class)  #指定位置插入



#>>>>>>>>>>>>>计算总分 = 语文 + 数学 + 英语
#new_datas[['语文','数学','英语']].astype(int)

new_datas["总分"] = new_datas[["语文","数学","英语"]].apply(lambda x: x.sum(), axis=1)
new_datas["平均分"] = new_datas[["语文","数学","英语"]].apply(lambda x: x.mean(), axis=1).astype(int)






#>>>>>>>>>>>>>加附加分的总分

def score(grade):
	grade = grade + np.random.randint(0,6)
	return grade

new_datas['附加总分'] = new_datas['总分'].apply(score)    #加上附加分

#>>>>>>>>>>>>>计算各个科目平均成绩
means = new_datas[['语文','数学','英语','总分','附加总分']].mean().astype(int)
#print(means)


#>>>>>>>>>>>>>条件计算 是否本科上线
array_new = np.array(new_datas)

result = np.where(array_new[:,-1] > 311,'合格','不合格')

new_datas["结果"] = result


#print(new_datas)






#>>>>>>>>>>>>>分类统计
info_1 = new_datas.groupby(['性别']).agg({'总分':["sum","mean"]})

info_2 = new_datas.groupby(['性别']).agg({'总分':["sum","mean"],'附加总分':["sum","mean"]})

info_3 = new_datas.groupby(['性别','分科']).agg({'总分':["sum","mean"]})

#print(info_3)


#>>>>>>>>>>>>>条件筛选

result_1 = new_datas[(new_datas["分科"] == "文科") & (new_datas["性别"] == '男')] #找出文科班男生的所有数据

#print(result_1)

result_2 = new_datas[(new_datas['性别'] == '女') & (new_datas['总分'] >= 340 )][["姓名","学号"]]   #找出女生过一本线的姓名和学号
#print(result_2)
#print(new_datas)



#>>>>>>>>>>>>>排序

new_datas_sort = new_datas.sort_values("附加总分",ascending=True)  #ascending=True升序降序
#print(new_datas_sort)


#new_datas.to_csv("new_grades.csv",encoding="gb2312")