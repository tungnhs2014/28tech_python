class SoPhuc:
    def __init__(self, thuc, ao):
        self.thuc = thuc
        self.ao = ao
    def __add__(self, other):
        tmp1 = self.thuc + other.thuc
        tmp2 = self.ao + other.ao
        return SoPhuc(tmp1, tmp2)
    def __eq__(self, other):
        return self.thuc == other.thuc and self.ao == other.ao
    def __str__(self):
        return f'{self.thuc} + {self.ao}j'
        
if __name__ == '__main__':
    s1 = SoPhuc(2, 3)
    s2 = SoPhuc(2, 3)
    s3 = s1 + s2
    print(s1)
    print(s3)
    print(s1 == s3)
    print(s1 == s2)