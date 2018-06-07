for(all in 1:42){ 
  
  #Load the file to a dataframe
  link2<-toString(all)
  link2<-paste('/Users/maribelojeda/MIT/I-WALKER/i-walker-Atia/terceranalisis/Straightpath/cvi', link2,'.mat.csv', sep = "")
  link4<-toString(link2)
  fl<-read.csv(link4, header = TRUE, sep = "," ) 
  fl<- as.data.frame(fl) 
  
  #Create a new array with the distance travelled 
  dist <- fl[11]
  dist2 <-array(length(dist))
  
  fexl <-array(length(dist))
  fexr <-array(length(dist))
  feyl <-array(length(dist))
  feyr <-array(length(dist))
  fezl <-array(length(dist))
  fezr <-array(length(dist))
  
  
  dist2[1]<-dist[1,1]
  dist2[length(dist[,1])]<-0
  fexl[1] <-dist2[1]+fl[1][1,1]
  fexr[1] <-dist2[1]+fl[2][1,1]
  feyl[1] <-dist2[1]+fl[3][1,1]
  feyr[1] <-dist2[1]+fl[4][1,1]
  fezl[1] <-dist2[1]+fl[5][1,1]
  fezr[1] <-dist2[1]+fl[6][1,1]
  
  fexl[length(dist[,1])] <-fl[1][length(dist[,1]),1]
  fexr[length(dist[,1])] <-fl[2][length(dist[,1]),1]
  feyl[length(dist[,1])] <-fl[3][length(dist[,1]),1]
  feyr[length(dist[,1])] <-fl[4][length(dist[,1]),1]
  fezl[length(dist[,1])] <-fl[5][length(dist[,1]),1]
  fezr[length(dist[,1])] <-fl[6][length(dist[,1]),1]
  
  for(i in 2:length(dist[,1])-1){
    dist2[i]<-(dist[i+1,1]-dist[i,1])*100
    fexl[i] <-dist2[i]+fl[1][i,1]
    fexr[i] <-dist2[i]+fl[2][i,1]
    feyl[i] <-dist2[i]+fl[3][i,1]
    feyr[i] <-dist2[i]+fl[4][i,1]
    fezl[i] <-dist2[i]+fl[5][i,1]
    fezr[i] <-dist2[i]+fl[6][i,1]
  }
  
  fl[ , 'travelled'] <- dist2
  fl[ , 'fexl'] <- fexl
  fl[ , 'fexr'] <- fexr
  fl[ , 'feyl'] <- feyl
  fl[ , 'feyr'] <- feyr
  fl[ , 'fezl'] <- fezl
  fl[ , 'fezr'] <- fezr
  
  #Print result
  write.table(fl  , file=link4, row.names = FALSE,  col.names = TRUE, sep = ",")
  
}