import sys
class Rectangle:
    def __init__(self,dai,rong,mau):
        self.dai = dai;
        self.rong = rong
        self.mau = mau.capitalize()
    def perimeter(self):
        return (self.dai+self.rong)*2
    def area(self):
        return self.dai*self.rong
    def color(self):
        return self.mau

# a,b,c = [str(x) for x in input().split()]
# print(a,b,c.capitalize())
arr = input().split()
if(int(arr[0])>0 and int(arr[1])>0):
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
else:
    print('INVALID')
sys.exit()
if __name__ == '__main__':
    arr = input().split()
    r = Rectangle(int(arr[0]), int(arr[1]), int(arr[2]))
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
