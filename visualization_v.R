#With this code we aim to create the visualizations. We want to compare:
#Age vs ForcesMean and clusters, age vs velocityMean and clusters, age vs ForcesCV and clusters, age vs velocityCV and clusters
#Age vs ForcesMean vs ForcesSD and clusters, Age vs velocityMean vs velocitySD and clusters
#Age vs ForcesMean vs VelocityMean and clusters



base<-read.csv('/Users/maribelojeda/Desktop/MIT/I-WALKER/i-walker-Atia/terceranalisis/visualization_base_5.csv', header = TRUE, sep = "," ) 
base <- as.data.frame(base) #We transpose the dataframe of the csv document 
basem<-subset(base, base$Age>65)

library(plotly)
library(ggplot2)
library("scatterplot3d") # load

#Lineal velocity

plot_ly(base, y= ~lhfzMean, x= ~X...ID, color = ~Cluster, symbol = ~Cluster, symbols = c('circle','square',18,'circle','square',18))%>%  
  layout(title = 'Comparison of the left z-forces mean vs lineal velocity mean per cluster')

plot_ly(base, y= ~velMean, x= ~X...ID, color = ~Cluster, symbol = ~Cluster, symbols = c('circle','square',18,'circle','square',18))%>%  
  layout(title = 'Comparison of the left z-forces mean vs lineal velocity mean per cluster')

plot_ly(base, x= ~lhfzMean, y= ~velMean, color = ~Cluster, symbol = ~Cluster, symbols = c('circle','square',18,'circle','square',18))%>%  
  layout(title = 'Comparison of the left z-forces mean vs lineal velocity mean per cluster')

plot_ly(base, z= ~lhfzMean, y= ~velMean, x= ~Age, color = ~Cluster, colors = "Set1", symbol = ~Cluster, symbols = c('circle','square',18,'circle','square',18))%>%  
  layout(title = 'Comparison of the left z-forces mean vs lineal velocity mean vs age per cluster')

plot_ly(base, z= ~rhfzMean, y= ~rhfyMean, x= ~rhfxMean, color = ~Cluster, colors = "Set1", symbol = ~Cluster, symbols = c('circle','square',18,'circle','square',18))%>%  
  layout(title = 'Comparison of the right forces mean in x, y and z')

plot_ly(base, z= ~rhfzMean, y= ~rhfzSD, x= ~Age, color = ~Cluster, colors = "Set1", symbol = ~Cluster, symbols = c('circle','square',18,'circle','square',18))%>%  
  layout(title = 'Comparison of the righ z-forces mean vs standar deviation vs age per cluster')

plot_ly(base, z= ~rhfzMean, y= ~rhfzSD, x= ~X...ID, color = ~Cluster, colors = "Set1", symbol = ~Cluster, symbols = c('circle','square',18,'circle','square',18))%>%  
  layout(title = 'Comparison of the righ z-forces mean vs standar deviation vs UID per cluster')

plot_ly(base, z= ~rhfzMean, y= ~rhfzSD, x= ~rhfzCV, color = ~Cluster, colors = "Set1", symbol = ~Cluster, symbols = c('circle','square',18,'circle','square',18))%>%  
  layout(title = 'Comparison of the righ z-forces mean vs standar deviation vs coefficient of variation per cluster')

plot_ly(base, z= ~rhfzMean, y= ~lhfzMean, x= ~velMean, color = ~Cluster, colors = "Set1", symbol = ~Cluster, symbols = c('circle','square',18,'circle','square',18))%>%  
  layout(title = 'Comparison of the righ z-forces mean vs left z-forces mean vs age per cluster')

plot_ly(base, x= ~rhfzMean, y= ~lhfzMean, color = ~Cluster, symbol = ~Cluster, symbols = c('circle','square',18,'circle','square',18))%>%  
  layout(title = 'Comparison of the righ z-forces mean vs left z-forces mean per cluster')

plot_ly(base, z= ~rhfzMean, y= ~rhfzSD, x= ~Stride, color = ~Cluster, colors = "Set1", symbol = ~Cluster, symbols = c('circle','square',18,'circle','square',18))%>%  
  layout(title = 'Comparison of the righ z-forces mean vs standar deviation vs UID per cluster')

plot_ly(base, z= ~rhfzMean, y= ~Age, x= ~Stride, color = ~Cluster, colors = "Set1", symbol = ~Cluster, symbols = c('circle','square',18,'circle','square',18))%>%  
  layout(title = 'Comparison of the righ z-forces mean vs standar deviation vs UID per cluster')

plot_ly(base, z= ~rhfzMean, y= ~Age, x= ~Stride, color = ~Cluster, colors = "Set1", symbol = ~Cluster, symbols = c('circle','square',18,'circle','square',18))%>%  
  layout(title = 'Comparison of the righ z-forces mean vs standar deviation vs UID2 per cluster2')


#paper
plot_ly(base, y= ~rhfzMean, x= ~Age, color = ~Cluster, colors = "Set1", mode = "markers", marker = list(size = 13 ))%>%  
  layout(title = 'Comparison of the righ z-forces mean vs standar deviation vs UID2 per cluster2')

plot_ly(base, y= ~rhfzMean, x= ~rhfzSD, color = ~Cluster, colors = "Dark2",  mode = "markers", symbol = ~AgeN, symbols = c('circle','square',18,'x','triangle-up',"star-dot",'triangle-down','bowtie'),  mode = "markers", marker = list(size = 18 ))%>%  
  layout(title = 'Comparison of the righ z-forces mean vs standar deviation vs UID2 per cluster2')

plot_ly(base, y= ~rhfzMean, x= ~velMean, color = ~Cluster, colors = "Dark2", symbol = ~AgeN, symbols = c('circle','square',18,'x','triangle-up',"star-dot",'triangle-down','bowtie'),  mode = "markers", marker = list(size = 18 ))%>%
  layout(title = 'Comparison of the righ z-forces mean vs standar deviation vs UID2 per cluster2')

plot_ly(base, y= ~rhfzMean, x= ~Age, color = ~Cluster, colors = "Dark2", symbol = ~TINETIN, symbols = c('triangle-down',"star-dot",'triangle-up','O'),  mode = "markers", marker = list(size = 18 ))%>%
  layout(title = 'Comparison of the righ z-forces mean vs standar deviation vs UID2 per cluster2')





#plot_ly(base, x=~rhfzMean, y = ~rhfzSD, text = ~Cluster, type = 'scatter', mode = 'markers',
  #marker = list(size = ~rhfzSD, opacity = 0.5)) %>%
  #layout(title = 'Gender Gap in Earnings per University')

base1<- subset(base,Age.D=='Y')
base2<- subset(base,Age.D=='M')
base3<- subset(base,Age.D=='O')

#plot_ly(x = base$rhfzCV, type = "histogram")%>%
  #layout(title = 'Histogram of the distribution of the mean of the right forces on Z')

#plot_ly(alpha = 0.6) %>%
  #add_histogram(x = base1$rhfzCV, name='<60') %>%
  #add_histogram(x = base2$rhfzCV, name='60>75') %>%
  #add_histogram(x = base3$rhfzCV,, name='>75') %>%
  #layout(barmode = "overlay",title = 'Histogram of the distribution of the mean of the right forces on Z per age')

 