import numpy as np
import fastcluster


def dist(R):
	N = R.shape[0]
	d = R[np.triu_indices(N,1)]
	out = fastcluster.average(d).astype(int)

	#Genealogy Set
	dend = {i: (np.array([i]),) for i in range(N)}
	for i,(a,b,_,_) in enumerate(out):
		dend[i+N] = (np.concatenate(dend[a]),np.concatenate(dend[b]))


	[dend.pop(i,None) for i in range(N)]

	return dend.values()

def AvLinkC(Dend,R):

	N = R.shape[0]
	Rs = np.zeros((N,N))

	for (a,b) in Dend:
		Rs[np.ix_(a,b)] = R[a][:,b].mean()

	Rs = Rs+Rs.T

	np.fill_diagonal(Rs,1)
	return Rs	
    
def noise(N,T,epsilon=1e-10):
    return np.random.normal(0,epsilon ,size=(N,T))

def filterCorrelation(x,Nboot=100):

	N,T = x.shape
	rT = range(T)
	ns = noise( N,T ) 

	Cbav = np.zeros((N,N))
	for _ in range(Nboot):
		xboot = x[:,np.random.choice(rT,size=T,replace=True)] + ns
		Cboot  = np.corrcoef(xboot)
		Dend = dist(1-Cboot)
		Cbav += AvLinkC(Dend,Cboot)

	Cbav = Cbav/Nboot
	return Cbav

def filterCovariance(x,Nboot=100):

	N,T = x.shape
	rT = range(T)
	ns = noise( N,T ) 


	Sbav = np.zeros((N,N))
	for _ in range(Nboot):
		xboot = x[:,np.random.choice(rT,size=T,replace=True)] + ns
		Cboot  = np.corrcoef(xboot)
		Dend = dist(1-Cboot)
		std = xboot.std(axis=1)
		Sbav += AvLinkC(Dend,Cboot)*np.outer(std,std)

	Sbav = Sbav/Nboot
	return Sbav


def filterCovarianceArmonic(x,Nboot=100):

	N,T = x.shape
	rT = range(T)
	ns = noise( N,T ) 

	Sbav = np.zeros((N,N))
	for _ in range(Nboot):
		xboot = x[:,np.random.choice(rT,size=T,replace=True)] + ns
		Cboot  = np.corrcoef(xboot)
		Dend = dist(1-Cboot)
		std = xboot.std(axis=1)
		Sbav += np.linalg.pinv(AvLinkC(Dend,Cboot)*np.outer(std,std))

	Sbav = Sbav/Nboot
	return np.linalg.pinv(Sbav)

def HigherOrder(C,Norder):
    Cf = np.zeros(C.shape)
    for _ in range(Norder):
        res = C - Cf
        dend = dist(1-res)
        res = AvLinkC(dend,res)
        np.fill_diagonal(res,0)
        Cf += res

    np.fill_diagonal(Cf,1)
    return Cf

def no_neg(x):
    l,v = np.linalg.eigh(x)
    p = l>0
    l,v = l[p],v[:,p]
    return np.dot(v*l,v.T)

def near(x,niter=100,eigtol=1e-6,conv=1e-8):
    
    D = np.zeros(x.shape)
    diag = x.diagonal()

    for _ in range(niter):

        y = x
        R = x - D
        x = no_neg(R)
        D = x - R
        np.fill_diagonal(x,diag)
        
        if np.linalg.norm(x-y,ord=np.inf)/np.linalg.norm(y,ord=np.inf)<conv:
            break
    else:
        print "it didn't converge"
    return x

def filterCovarianceHO(x,Nboot=100,k=3,method='no-neg'):
    
    f = {'no-neg':no_neg, 'near':near}
    
    N,T = x.shape
    ns = noise(N,T)
    rT = range(T)
    C = np.zeros((N,N))
    for _ in range(Nboot):
        xboost = x[:,np.random.choice(rT,size=T,replace=True)] + ns
        Rb = np.corrcoef(xboost)
        s = xboost.std(axis=1)
        C += f[method](HigherOrder(Rb,k) * np.outer(s,s))
    return C/Nboot
    
'''
if __name__=='__main__':
	x = np.random.normal(0,1,size=(10,100))
	print(filterCovarianceHO(x,method='near'))
'''
