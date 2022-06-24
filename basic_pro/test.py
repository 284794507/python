# -*- coding: utf-8 -*-

def triangles(): 
    lst = [1]
    while lst:
        yield(lst)
        new_lst = lst[:] #[x for x in lst]
        new_lst.append(0)
        new_lst.insert(0,0)
        lst = []
        for index,item in enumerate(new_lst):
            if index > 0:
                lst.append(new_lst[index-1] + new_lst[index])
