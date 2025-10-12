# import numpy as np
# def normalize(x):
#     fac= abs(x).max()
#     x_n=x/x.max()
#     return fac,x_n
#     x= np.array([1,1,1])
#     a= np.array([[1,1,3],[1,5,1],[3,1,1]])
# for i in range(10):
#     x= np.dot(a,x)
#     lambda_1,x= normalize(x)
# print("Eigen value :",lamda_1)
# print("Eigen vector :",x)

# # from sympy import*
# # x,y,z= symbols('x,y,z')
# # u= x**2+y**2+z**2
# # v= x*y+y*z+z*x
# # w=x+y+z
# # A= Matrix([u,v,w])
# # J= det(A.jacobian([x,y,z]))
# # print("Jacobian (u,v,w) =",J)

# # from sympy import*
# # x,y,a= symbols('x,y,a')
# # F= x**3 + y**3 - 3*a*x*y
# # display("The given function is F = ",F)
# # F_x=diff(F,x)
# # F_y=diff(F,y)
# # F_xx=diff(F,x,x)
# # F_yy=diff(F,y,y)
# # F_xy=diff(F,x,y)
# # display("F-x=",F_x,"F-y",F_y)
# # display("F-xx=",F_xx,"F-yy",F_yy,"F-xy=",F_xy)

from sympy import*
x,y,c= symbols('x,y,c')
y=c**2/x
y1= diff(y,x)
y2= diff(y,x,2)
R= simplify((1+y1**2)**(3/2)/y2)
print("Radius of curvature is R = ",R)

# # from sympy import*
# # a,t= symbols('a,t')
# # r= a*(1-cos(t))
# # r1= diff(r,t)
# # Phi=atan(r/r1)
# # Phi=Phi.subs(t,pi/6)
# # display("The angle between radius vector and tangent is",Phi)

# #  Eigen values and eigen vectors
# # from sympy import *
# # A = Matrix ([[1,1,3],[1,5,1],[3,1,1]])
# # display ("The given matrix is ",A)
# # Eigen_values = A.eigenvals()
# # Eigen_vectors = A.eigenvects()
# # display("The Eigen values  are ",Eigen_values)
# # display("The Eigen vectors are",Eigen_vectors)

f1 = lambda x,y,z:(12-y-z)/10
f2 = lambda x,y,z:(12-x-z)/10
f3 = lambda x,y,z:(12-x-y)/10
x0=0
y0=0
z0=0
x1 = f1 (x0,y0,z0)
y1 = f2 (x1,y0,z0)
z1 = f3 (x1,y1,z0)
print('\n1 : x1=%0.4f,y1=%0.4f,z1=%0.4f\n'%(x1,y1,z1))
x2 = f1 (x1,y1,z1)
y2 = f2 (x2,y1,z1)
z2 = f3 (x2,y2,z1)
print("\n2 : x2=%0.4f,y2=%0.4f,z2=%0.4f\n"%(x2,y2,z2))
x3 = f1 (x2,y2,z2)
y3 = f2 (x3,y2,z2)
z3 = f3 (x3,y3,z2)
print("\n3 : x3=%0.4f,y3=%0.4f,z3=%0.4f\n"%(x3,y3,z3))

# # Rank of a matrix
# # from sympy import*
# # A = Matrix ([[2,-1,-3,-1],[1,2,3,-1],[1,0,1,1],[0,1,1,-1]])
# # display("The given matrix is ",A)
# # R= A.rank()
# # print("The rank is ",R)

def gcd1(a,b):
    c=1
    if b<a:
        a,b=b,a
    while(c>0):
        c=b%a;
        print(a,c);
        b=a;
        a=c;
        continue
    print("GCD = ",b);
gcd1(32,54)

# from sympy import*
# a=int(input("Enter integer a :")):
# b=int(input("Enter integer b :")):

# m=int(input("Enter integer m :")):
# d=gcd(a,m)
# if (b%d!=0):
#     print("The congruence has no integer solution ")
# else:
#     for i in range(1,m-1):
#         x=(m/a)*i+(b/a)
#         if (x//1=x):
#             print("The solution of congruence is :",x)
#             break
