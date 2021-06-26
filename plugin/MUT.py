"""
Mango's Utility Tools (MUT)


CC BY-NC-SA 3.0 TW
    his is a human-readable summary of (and not a substitute for) the license.
    (https://creativecommons.org/licenses/by-nc-sa/3.0/tw/legalcode)
"""

from json import load, dump
from datetime import datetime
from random import randint

class MUT:
    def save(path:str, data:dict, encode:str='utf8'):
        try:
            with open(path, mode='w', encoding=encode) as file:
                dump(data, file, indent=4, ensure_ascii=False)
        except: raise IndexError
    
    def load(path:str, encode:str):
        try:
            with open(path, mode='r', encoding=encode) as file:
                return load(file)
        except: raise IndexError
    
    def now(prefix:str='[', suffix:str=']', format:str='%Y/%m/%d %H:%M:%S'):
        return f'{prefix}{datetime.now().strftime(format)}{suffix}'
    
    def randomCode(longer:int, digit:int):
        codeList = []
        rangeMax = int('F'*digit, 16)
        for i in range(longer):
            num = str(hex(randint(0, rangeMax)).replace('0x', '')).zfill(digit)
            codeList.append(num)
        code = '-'.join(codeList)
        return code

    def item_spawn(weight:dict, nullItem:str=None):
        # Check Weight
        check = sum([weight[i]*100 for i in weight])
        if check > 100:
            return
        for i in weight:
            if weight[i]*100 not in range(1, 101):    
                return

        # Index
        items = []
        for i in weight:
            for j in range(int(weight[i]*100)):
                items.append(i)

        # Check null item
        if len(items) < 100:
            for i in range(100-len(items)):
                items.append(nullItem)
        return items

    def isfloat(num):
        try: num = float(num)
        except: return False
        return True if num % 1 else False
    
    def round(num:int):
        if num % 1 >= 0.5:
            return int(num//1+1)
        return int(num)