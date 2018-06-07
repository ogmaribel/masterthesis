for(all in 1:42){ 
  #Load the file to a dataframe
  link2<-toString(all)
  link3<-link2
  link2<-paste('/Users/maribelojeda/MIT/I-WALKER/i-walker-Atia/terceranalisis/tsmeter/cvi', link2,'_meter.csv', sep = "")
  link4<-toString(link2)
  fl<-read.csv(link4, header = TRUE, sep = "," ) 
  fl<- as.data.frame(fl) 
  
  plot.ts(fl$speed, ylim=c(0,2), col= 'red', pch='l',main = link3, cex.main=1)
  
  plot.ts(fl$acc, ylim=c(-.3,.3), col= 'blue', pch='l',main = link3, cex.main=1)
  abline(h=0, col="red")
}