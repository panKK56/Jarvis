from buildin.Chrome import ChromeList
# import selenium as s

class Trash_Parce:

    @staticmethod
    def check_if_any_in_str(lis: list, st: str):
#[1,2,3,4,5] #Q = "ARTTT" =>FALSE
#[1,2,3,4,5] #Q = "1hwiejh2eg" =>TRUE
        for i in lis:
            if i in st:
                return True
        return False

    @staticmethod
    def check_if_all_in_str(lis: list, st: str):
#["hii","my","name"] #Q hii my pankaj==>FALSE
#["hii","my","name"] #Q hii my name is pankaj==>True
        for i in lis:
            if type(i) is list:
                if not Trash_Parce.check_if_any_in_str(i, st):
                    return False
            else:
                if i not in st:
                    return False
        return True
#Q = open new tab
def ChromeCode(query):
    for _, lists in ChromeList.items():
        A = Trash_Parce.check_if_all_in_str(lists, query)
        if A:
            return _
    return False