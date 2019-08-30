#=======================================================================
# Estimering for nedbørsdataene  (jf eks 2 i introduksjonsforelesningen)
#=======================================================================

# Leser dataene fra fil. De gir nedbør (i mm) hver av de 92 dagene i mai-juli 2016
nedbor.blindern=read.table("https://www.uio.no/studier/emner/matnat/math/STK1110/data/nedbor-blindern.txt",header=T)

# Tar bare med de 54 dagene det regnet:
regn=nedbor.blindern$nedbor[nedbor.blindern$nedbor>0]


#===========================
# Beregner momentestimatene
#===========================

n=length(regn)
mom.alfa=mean(regn)^2/sum((regn-mean(regn))^2/n)
mom.beta=sum((regn-mean(regn))^2/n)/mean(regn)
c(mom.alfa,mom.beta)


#==================================
# Plotter log-likelihood funksjonen
#==================================

# Funksjon som beregner log-likelihooden:
loglik=function(alfa,beta)
{
  -n*alfa*log(beta)-n*lgamma(alfa)+(alfa-1)*sum(log(regn))-sum(regn)/beta
}
  
# Plotter log-likelihood funksjonen:
alfa=seq(0.4,1,0.01)
beta=seq(4,14,0.1)
f=outer(alfa,beta,loglik)
persp(alfa, beta, f, theta = 30, phi = 30, expand = 0.5, col = "lightblue")

# Konturplott av log-likelihooden
contour(alfa, beta, f, nlevels=20)


#========================================
# Bestemmer maximum likelihood estimatene 
#========================================

# Funksjon som beregner den negatve log-likelihooden:

negloglik=function(x)
{
  alfa=x[1]
  beta=x[2]
  -loglik(alfa,beta)
}

# Maksimerer log-likelihooden (ved å minimere den negative log-likelihooden numerisk):

ml.est=optim(c(mom.alfa,mom.beta),negloglik)  
ml.est$par  

