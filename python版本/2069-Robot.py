class Robot:

    def __init__(self, width: int, height: int):
        self.width = width 
        self.height = height 
        self.cur_dir = 'East'
        self.cur_pos = [0,0]
        self.directs = {
            'East': 'North',
            'North': 'West',
            'West': 'South',
            'South': 'East'
        }
        self.limits = {
            'East': self.width-1,
            'North': self.height-1,
            'West': self.width-1,
            'South': self.height-1
        }
        self.rl = 2 * (self.width+self.height-2)


    def step(self, num: int) -> None:
        # 需要预处理这个num
        num = (num-1)%self.rl +1
        while num > 0:
            # east: width - cur_pos[0]
            # north: height - cur_pos[1]
            # west: cur_pos[0]
            # south: cur_pos[1]
            dist = 0
            if self.cur_dir == 'East':
                dist = self.limits['East'] - self.cur_pos[0]
                #print('dist:',dist)
                if num <= dist:
                    self.cur_pos[0] += num
                    break
                else:
                    #在当前方向上前行完毕
                    num -= dist
                    self.cur_pos[0] = self.width - 1
                    self.cur_dir = self.directs[self.cur_dir] #转换方向
            elif self.cur_dir == 'North':
                dist = self.limits['North'] - self.cur_pos[1]
                #print('dist:',dist)
                if num <= dist:
                    self.cur_pos[1] += num 
                    break
                else:
                    num -= dist
                    # if num >= self.rl:
                    #     num = num % self.rl
                    #     continue
                    self.cur_pos[1] = self.height - 1
                    self.cur_dir = self.directs[self.cur_dir]
            elif self.cur_dir == 'West':
                dist = self.cur_pos[0]
                #print('dist:',dist)
                if num <= dist:
                    self.cur_pos[0] -= num 
                    break
                else:
                    num -= dist
                    # if num >= self.rl:
                    #     num = num % self.rl
                    #     continue
                    self.cur_pos[0] = 0
                    self.cur_dir = self.directs[self.cur_dir]
            else:
                dist = self.cur_pos[1]
                #print('dist:',dist)
                if num <= dist:
                    self.cur_pos[1] -= num 
                    break
                else:
                    num -= dist 
                    # if num >= self.rl:
                    #     num = num % self.rl
                    #     continue
                    self.cur_pos[1] = 0
                    self.cur_dir = self.directs[self.cur_dir]
        # print('after move:',self.cur_pos)

    def getPos(self) -> List[int]:
        return self.cur_pos

    def getDir(self) -> str:
        return self.cur_dir
    

# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()