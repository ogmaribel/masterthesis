#With this code we aim to create the visualizations. We want to compare:
#Age vs ForcesMean and clusters, age vs velocityMean and clusters, age vs ForcesCV and clusters, age vs velocityCV and clusters
#Age vs ForcesMean vs ForcesSD and clusters, Age vs velocityMean vs velocitySD and clusters
#Age vs ForcesMean vs VelocityMean and clusters



base<-read.csv('/Users/maribelojeda/MIT/I-WALKER/i-walker-Atia/terceranalisis/visualization_base.csv', header = TRUE, sep = "," ) 
base <- as.data.frame(base) #We transpose the dataframe of the csv document 

library(plotly)
library(ggplot2)
library("scatterplot3d") # load


plot_ly(base, z= ~lhfzMean, y= ~rhfzMean, x=~X...ID, color = ~Cluster)%>%  
  layout(title = 'Comparison of the left and right z-forces mean per cluster and user')

plot_ly(base, z= ~lhfzMean, y= ~rhfzMean, x=~Age, color = ~Cluster)%>%  
  layout(title = 'Comparison of the left and right z-forces mean per cluster and age')

plot_ly(base, z= ~lhfzCV, y= ~rhfzCV, x=~X...ID, color = ~Cluster)%>%  
  layout(title = 'Comparison of the left and right z-forces CV per cluster and user')

plot_ly(base, z= ~lhfzCV, y= ~rhfzCV, x=~Age, color = ~Cluster)%>%  
  layout(title = 'Comparison of the left and right z-forces CV per cluster and age')%>% 

plot_ly(base, z= ~rhfzMean, y= ~rhfzSD, x=~X...ID, color = ~Cluster)%>%  
  layout(title = 'Comparison of the righ force mean vs SD per cluster and user')

plot_ly(base, z= ~rhfzMean, y= ~rhfzSD, x=~Age, color = ~Cluster)%>%  
  layout(title = 'Comparison of the right force mean vs SD per cluster and age')

plot_ly(base, z= ~rhfzMean, y= ~rhfzSD, x=~rhfzCV, color = ~Cluster)%>%  
  layout(title = 'Comparison of the right force mean vs SD vs CV per cluster')

plot_ly(base, z= ~sumforcesMean, y= ~sumforcesSD, x=~sumforcesCV, color = ~Cluster)%>%  
  layout(title = 'Comparison of the sumformces mean vs SD vs CV per cluster')

plot_ly(base, z= ~sumforcesMean, y= ~sumforcesSD, x=~Age, color = ~Cluster)%>%  
  layout(title = 'Comparison of the sumformces mean vs SD vs CV per age')

plot_ly(base, z= ~rhfzMean, y= ~rhfzSD, x=~X...ID, color = ~Cluster)%>%  
  layout(title = 'Comparison of the right z-forces mean vs SD vs User per cluster')

plot_ly(base, z= ~rhfzMean, y= ~rhfyMean, x=~rhfxMean, color = ~Cluster)%>%  
  layout(title = 'Comparison of the right forces mean x vs y vs z per cluster')

plot_ly(base, y= ~rhfzSD, x=~rhfzCV, color = ~Cluster)%>%  
  layout(title = 'Comparison of the right force SD vs CV per cluster')

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

 