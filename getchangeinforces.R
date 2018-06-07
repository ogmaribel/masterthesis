library(plotly)
packageVersion('plotly')
#plot_ly(x=c(1:length(fzl[,1])), y= c(1:length(fzl[,1])),type = 'scatter', mode = 'lines')
 
fz<-employee <- c('ChangeinForceZ')

#printdf<-data.frame(fz)


#Plot time series
cluster<-read.csv('/Users/maribelojeda/MIT/I-WALKER/i-walker-Atia/terceranalisis/cviclustering.csv', header = TRUE, sep = "," )

all=1
  
  #Load the file to a dataframe
  link2<-toString(all)
  link3<-link2
  link2<-paste('/Users/maribelojeda/MIT/I-WALKER/i-walker-Atia/terceranalisis/Straightpath/cvi', link2,'.mat.csv', sep = "")
  link4<-toString(link2)
  fl<-read.csv(link4, header = TRUE, sep = "," ) 
  fl<- as.data.frame(fl) 
  
  fzl <- fl[5]
  fzr <- fl[6]
  fz<-data.frame(fzl, fzr) 
  

p1<-plot_ly(y=fz$Var1_.5, x= c(1:length(fzl[,1]))) %>%
  layout(xaxis =list(range=c(0,50000)), yaxis =list(range=c(-90,10))) %>%
  add_lines(name = ~"Left") 
  

p2<-plot_ly(y=fz$Var1_.6, x= c(1:length(fzl[,1]))) %>%
  layout(xaxis =list(range=c(0,50000)), yaxis =list(range=c(-90,10)), title= paste('cvi',all)) %>%
  add_lines(name = ~"Right") 

subplot(p1, p2)
