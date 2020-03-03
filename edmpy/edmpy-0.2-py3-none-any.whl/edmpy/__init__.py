from sympy import *

X = []
Y = []
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

xhat = "x\u0302"
yhat = "y\u0302"
zhat = "z\u0302"
x = Symbol('x')
y = Symbol('y')
z = Symbol('z')


def gradient(inp=0,printn=1,inp_str=""):
	#from mpl_toolkits.mplot3d import axes3d
	#import matplotlib.pyplot as plt
	#import numpy as np
	check = 0
	start = "\033[1m"
	end = "\033[0;0m"
	symexpr = inp_str
	if inp==0:
		print("This is the gradient evaluator of polynomial fields. Use the following instructions to evaluate the gradient...")
	#exnum = input("Enter the number of expressions seperated by '+' symbols")
	#Enter expressions in the form of coefficient, symbol and power in that order and enter the word 'end' to terminate
	#the expression
		symexpr = input("Enter expression\n")
	print(' ')
	expr = sympify(symexpr)
	a = diff(expr,x,1)
	#Uncomment the following lines to get colored outputs
	#astr = "("+str(a)+")" + color.BOLD + color.RED + xhat + color.END + color.END
	astr = "("+str(a)+")" + xhat
	b = diff(expr,y,1)
	#bstr = "("+str(b)+")" + color.BOLD + color.BLUE + yhat + color.END + color.END
	bstr = "("+str(b)+")" + yhat
	c = diff(expr,z,1)
	#cstr = "("+str(c)+")" + color.BOLD + color.YELLOW + zhat + color.END + color.END
	cstr = "("+str(c)+")" + zhat
	gexpr = astr + " + " + bstr + " + " + cstr
	grad = "\u2207r\u0302 = " + astr + " + " + bstr + " + " + cstr
	if printn==0:
		print(grad)
	out_grad = []
	out_grad.append(sympify(a))
	out_grad.append(sympify(b))
	out_grad.append(sympify(c))
	return out_grad
	#return gradient
	#grad = Add('(',a,b,c)
	#print(grad)

def divergence():
	print("This is the divergence evaluator. Use the following instructions to evaluate the divergence...")
	xcomp = input("Enter the " + xhat+ " component\n")
	xcomp = sympify(xcomp)
	ycomp = input("Enter the " + yhat+ " component\n")
	ycomp = sympify(ycomp)
	zcomp = input("Enter the " + zhat+ " component\n")
	zcomp = sympify(zcomp)
	print("The vector whose divergence is to be evaulated is\n")
	print("("+str(xcomp)+")"+xhat+" + ("+str(ycomp)+")"+yhat+" + ("+str(zcomp)+")"+zhat)
	p_xd = diff(xcomp,x,1)#Partial derivative wrt x
	p_yd = diff(ycomp,y,1)#Partial derivative wrt y
	p_zd = diff(zcomp,z,1)#Partial derivative wrt z
	print("\u2207 . r\u0302 = (" + str(p_xd) + ") + (" + str(p_yd) + ") + (" + str(p_zd) + ")\n")

def field_plot(yn=True,comps=[0,0,0],dim=2):
	from mpl_toolkits.mplot3d import axes3d
	import matplotlib.pyplot as plt
	
	global X
	global Y
	fig = plt.figure()
	xr = np.linspace(-30,30,15)
	yr = np.linspace(-30,30,15) 
	X,Y = np.meshgrid(xr, yr)
	U = X
	V = Y
	xcomp = comps[0]
	ycomp = comps[1]
	if yn==False:#If the user wants to provide input inside the function
		print("This is the field plotter. Use the following instructions to plot...")
		xcomp = input("Enter the field expression...")
		xcomp = sympify(xcomp)
		ycomp = input("Enter the field expression...")
		ycomp = sympify(ycomp)
	
	for i in range(len(xr)):
		for j in range(len(yr)):
			x1 = X[i,j]
			y1 = Y[i,j]
			U[i,j] = xcomp.subs({x:x1, y:y1})
			V[i,j] = ycomp.subs({x:x1, y:y1})


	plt.quiver(xr,yr,U,V, linewidth=1, units='width',angles='xy', scale_units='xy')#, scale = 1)
	plt.title("vector field")
	plt.show()


def curl(vec_inp,printn=1):
	xcomp = sympify(vec_inp[0])
	ycomp = sympify(vec_inp[1])
	zcomp = sympify(vec_inp[2])

	curl_x = diff(zcomp,y,1) - diff(ycomp,z,1)
	curl_y = diff(xcomp,z,1) - diff(zcomp,x,1)
	curl_z = diff(ycomp,x,1) - diff(xcomp,y,1)

	out_vec = [curl_x, curl_y, curl_z]
	if printn==0:
		print("\u2207 x r\u0302 = (" + str(curl_x) + ")" + xhat+ " + (" + str(curl_y) + ")" + yhat+ " + (" + str(curl_z) + ")" + zhat +"\n")
	return out_vec

