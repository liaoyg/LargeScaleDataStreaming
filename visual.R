rm(list=ls())
a=read.csv("result.csv",header=F,sep=";")
data1=as.matrix(a)[1:6,1:9]
rownames(data1)=c("balance","chunking","dgreedy","hashing","rgreedy","triangle")
data1=t(data1)
data11=data1[c(1,4,7),]
rownames(data11)=c("BFS","DFS","Random")
barplot(data11,main="DBLP, K=4", ylim=c(0,1),col=c("red","green","blue"),legend=NULL,beside=TRUE)  
legend("topright",rownames(data11),fill=c("red","green","blue"),cex=0.7)
#example
# counts <- table(mtcars$vs, mtcars$gear)
# barplot(counts, main="Car Distribution by Gears and VS",
#         xlab="Number of Gears", col=c("darkblue","red"),
#         legend = rownames(counts), beside=TRUE)

data2=as.matrix(a)[1:6,10:18]
rownames(data2)=c("balance","chunking","dgreedy","hashing","rgreedy","triangle")
data2=t(data2)
data22=data2[c(2,5,8),]
rownames(data22)=c("BFS","DFS","Random")
barplot(data22,main="Email, K=8", ylim=c(0,1),col=c("red","green","blue"),legend=NULL,beside=TRUE)  
legend("topright",rownames(data22),fill=c("red","green","blue"),cex=0.4)

data3=as.matrix(a)[1:6,19:27]
rownames(data3)=c("balance","chunking","dgreedy","hashing","rgreedy","triangle")
data3=t(data3)
data33=data3[c(3,6,9),]
rownames(data33)=c("BFS","DFS","Random")
barplot(data33,main="Facebook, K=12", ylim=c(0,1),col=c("red","green","blue"),legend=NULL,beside=TRUE)  
legend("topright",rownames(data33),fill=c("red","green","blue"),cex=0.3)

#BFS k=4 line segments
data4=as.matrix(a)[1:6,c(1,10,19)]
rownames(data4)=c("balance","chunking","dgreedy","hashing","rgreedy","triangle")
colnames(data4)=c("317080","36692","4039")
plot(x=rep(317080,6),y=data4[,1],xlim=c(3000,340000),ylim=c(0,1),xlab="data set size",ylab="fraction of edges cut")
points(x=rep(36692,6),y=data4[,2])
segments(x0=rep(36692,6),y0=data4[,2],x1=rep(317080,6),y1=data4[,1],col=1:6)
points(x=rep(4039,6),y=data4[,3])
segments(x0=rep(36692,6),y0=data4[,2],x1=rep(4039,6),y1=data4[,3],col=1:6)
legend("top",c("balance","chunking","dgreedy","hashing","rgreedy","triangle"),fill=1:6,cex=0.7)
