fz<-employee <- c('lx','rx','ly','ry','lz','rz','speed')
printdf<-data.frame(fz)
for(all in 1:42){ 
    #Load the file to a dataframe
    link2<-toString(all)
    link3<-link2
    link2<-paste('/Users/maribelojeda/MIT/I-WALKER/i-walker-Atia/terceranalisis/Straightpath/cvi', link2,'.mat.csv', sep = "")
    link4<-toString(link2)
    fl<-read.csv(link4, header = TRUE, sep = "," ) 
    fl<- as.data.frame(fl) 
    
    
    #Create a new column that separates the distance every meter walked
    dist <- fl[11]
    st<-1
    cl<-1
    mclust <-array(length(dist))
    mclust[1]<-cl
    
    for(i in 2:(length(dist[,1]))){
      cond<-dist[i,1]-dist[st,1]
      #print(paste(i,',',st,cond))
      
      if(cond > 1){
        mclust[i]<-cl
        st<-i
        cl<-cl+1
      }else{
        mclust[i]<-cl
      }
    }
    
    fl[ , "clase"] <- mclust
    
    
    
    #Split the 6 forces per cathegory #Check the average force per cathegory and stimate the work 
    mc<-unique(mclust)
    numb<-length(mc)
    mxl<-length(mc)
    mxr<-length(mc)
    myl<-length(mc)
    myr<-length(mc)
    mzl<-length(mc)
    mzr<-length(mc)
    
    speed<-length(mc)
    acc<-length(mc)
    
    
    for(i in 1:numb){
      subs<-subset(fl,clase==i)
      mxl[i] <- mean((subs[1])[,1])
      mxr[i] <- mean((subs[2])[,1])
      myl[i] <- mean((subs[3])[,1])
      myr[i] <- mean((subs[4])[,1])
      mzl[i] <- mean((subs[5])[,1])
      mzr[i] <- mean((subs[6])[,1])
      
      speed[i]<-sum(((subs[12])[,1])/100)/(length((subs[12])[,1])*.01)
      
    }
    
    acc[1]<-0
    
    for(i in 2:numb){
      subs2<-subset(fl,clase==i)
      subs3<-subset(fl,clase==(i-1))
      
      acc[i]<-(speed[i]-speed[i-1])/((length((subs2[12])[,1])*.01)+(length((subs3[12])[,1])*.01))
      print(((length((subs2[12])[,1])*.01)+(length((subs3[12])[,1])*.01)))
    }
    
    #Calculate the average work of all cathegories
    tseries<-data.frame(mxl, mxr, myl, myr, mzl, mzr, speed,acc)
    link5<-paste(paste('/Users/maribelojeda/MIT/I-WALKER/i-walker-Atia/terceranalisis/tsmeter/cvi', link3,'_meter.csv', sep = ""))
    write.table(tseries  , file=link5, row.names = FALSE,  col.names = TRUE, sep = ",")
    
    tp<-length(7)
    tp[1]<-mean(mxl)
    tp[2]<-mean(mxr)
    tp[3]<-mean(myl)
    tp[4]<-mean(myr)
    tp[5]<-mean(mzl)
    tp[6]<-mean(mzr)
    tp[7]<-mean(speed)
    
    nombre<-paste('cvi', toString(all), sep = "")
    printdf[ , nombre] <- tp
  
}
#Print result
write.table(printdf  , file='/Users/maribelojeda/MIT/I-WALKER/i-walker-Atia/terceranalisis/Straightpath/meanwork.csv', row.names = FALSE,  col.names = TRUE, sep = ",")
