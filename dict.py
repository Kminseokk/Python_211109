dict_a = {'id':1, 'name':'hong kildong', 'email':'hong@mail.com','hp_num':'010-2343-9870'}
dict_b = {'id':2, 'name':'lee soonsin', 'email':'lee@mail.com', 'hp_num':'010-3333-5555'}
dict_c = {'id':3, 'name':'jang youngsil', 'email':'jang@mail.com', 'hp_num':'010-7777-1234'}
dict_d = {'id':4, 'name':'king sejong','email':'king@mail.com', 'hp_num':'010-4567-0987'}


list_dict2 = (dict_a,dict_b,dict_c,dict_d)


for i in list_dict2:
    for k,v in i.items():
        print(k ,":",v)

