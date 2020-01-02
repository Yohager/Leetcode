class Solution:
    def simplifyPath(self, path: str) -> str:
        split_path = []
        for i in path.split('/'):
            if i == '..':
                if len(split_path) > 0:
                    split_path.pop(-1)
            else:
                if i != '.' and i != '':
                    split_path.append(i)
        return '/' + '/'.join(split_path)


if __name__ == "__main__":
    test = Solution
    path = '/a/../../b/../c//.//'
    print(test.simplifyPath(test,path))