class Solution:
    def give_char_cnt(self, str_):
        str_check = {}
        for _ in str_:
            if str_check.get(_):
                str_check[_] += 1
            else:
                str_check[_] = 1
        return str_check 
    def isAnagram(self, s: str, t: str) -> bool:
        s_check = self.give_char_cnt(s)
        t_check = self.give_char_cnt(t)
        character = set(list(s_check.keys())).union(set(list(t_check.keys())))
        print(character)
        print(s_check)
        print(t_check)

        if len(s_check) != len(t_check) and len(character)!=s_check:
            return False

        for _ in character:
            if s_check.get(_) and t_check.get(_):
                if s_check.get(_) != t_check.get(_):
                    return False
            else:
                return False

        return True