class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        '''
        2022.1.3 Monday
        '''
        weeks = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        d_offset = 1
        # day offset from today 
        d_offset = (d_offset + day - 3) % 7 
        # month offset from today 
        for i in range(month-1):
            d_offset = (d_offset + months[i]) % 7 
            if i == 1 and not year % 4 and (year % 100 or not year % 400):
                d_offset = (d_offset + 1) % 7 
        
        # year offset from today 
        if year < 2022:
            for j in range(year,2022):
                d_offset = (d_offset - (366 if not j % 4 and (j % 100 or not j % 400) else 365)) % 7 
        else:
            for j in range(2022,year):
                d_offset = (d_offset + (366 if not j % 4 and (j % 100 or not j % 400) else 365)) % 7 
        
        # print(d_offset)
        return weeks[d_offset]