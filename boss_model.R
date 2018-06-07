
base<-read.csv('/Users/maribelojeda/WalkAnalysis-master/dsdfz.csv', header = FALSE, sep = "," ) 
base <- as.data.frame(base) #We transpose the dataframe of the csv document 

    library(ggplot2)
    library(plotly)


    
print(plot_ly(base, x = ~V3, y = ~V1, z = ~V2,  colorscale = c('#FFE1A1', '#683531')))
    
 