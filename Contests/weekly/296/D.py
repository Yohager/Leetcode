class TextEditor:

    def __init__(self):
        self.t = ''
        self.cur = 0


    def addText(self, text: str) -> None:
        self.t = self.t[:self.cur] + text + self.t[self.cur:]
        self.cur += len(text)

    def deleteText(self, k: int) -> int:
        if self.cur >= k:
            self.t = self.t[:self.cur-k] + self.t[self.cur:]
            self.cur -= k 
            return k 
        else:
            # 不够删除
            self.t = self.t[self.cur:]
            v = self.cur
            self.cur = 0
            return v 

    def cursorLeft(self, k: int) -> str:
        if self.cur >= k:
            # 往左移动不够
            self.cur -= k 
            if self.cur >= 10:
                return self.t[self.cur - 10 : self.cur]
            else:
                return self.t[:self.cur]
        else:
            self.cur = 0
            return ''


    def cursorRight(self, k: int) -> str:
        n = len(self.t)
        if self.cur + k <= n:
            self.cur += k 
            if self.cur >= 10:
                return self.t[self.cur-10:self.cur]
            else:
                return self.t[:self.cur]
        else:
            self.cur = n 
            if self.cur >= 10:
                return self.t[self.cur-10:self.cur]
            else:
                return self.t[:self.cur]





# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)