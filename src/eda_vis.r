#load packages
library(tidyverse)
library(reshape2)
library(docopt)
library(caret)
library(testthat)
theme_set(theme_bw())

"Creates eda plots for the pre-processed training data from the Wisconsin breast cancer data (from http://mlr.cs.umass.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data).
Saves the plots as a pdf and png file.
Usage: src/eda_vis.r --X_train_path=<X_train_path> --y_train_path=<y_train_path>
  
Options:
--X_train_path=<X_train_path>     Path (including filename) to training data (which needs to be saved as a feather file)
--y_train_path=<y_train_path> Path to directory where the plots should be saved
" -> doc


opt <- docopt(doc)

#extra function 

## Function from User cybernetic at https://stackoverflow.com/questions/23891140/r-how-to-visualize-confusion-matrix-using-the-caret-package
draw_confusion_matrix <- function(cm) {
  
  layout(matrix(c(1,1,2)))
  par(mar=c(2,2,2,2))
  plot(c(100, 345), c(300, 450), type = "n", xlab="", ylab="", xaxt='n', yaxt='n')
  title('CONFUSION MATRIX', cex.main=2)
  
  # create the matrix 
  rect(150, 430, 240, 370, col='#1A64A7')
  text(195, 435, 'ASD Diagnosis', cex=1.2)
  rect(250, 430, 340, 370, col='#91C4DE')
  text(295, 435, 'No ASD Diagnosis', cex=1.2)
  text(125, 370, 'Predicted', cex=1.3, srt=90, font=2)
  text(245, 450, 'Actual', cex=1.3, font=2)
  rect(150, 305, 240, 365, col='#91C4DE')
  rect(250, 305, 340, 365, col='#1A64A7')
  text(140, 400, 'ASD Diagnosed', cex=1.2, srt=90)
  text(140, 335, 'No ASD Diagnosis', cex=1.2, srt=90)
  
  # add in the cm results 
  res <- as.numeric(cm$table)
  text(195, 400, res[1], cex=1.6, font=2, col='white')
  text(195, 335, res[2], cex=1.6, font=2, col='white')
  text(295, 400, res[3], cex=1.6, font=2, col='white')
  text(295, 335, res[4], cex=1.6, font=2, col='white')
  
  # add in the specifics 
  plot(c(100, 0), c(100, 0), type = "n", xlab="", ylab="", main = "DETAILS", xaxt='n', yaxt='n')
  text(10, 85, names(cm$byClass[1]), cex=1.2, font=2)
  text(10, 70, round(as.numeric(cm$byClass[1]), 3), cex=1.2)
  text(30, 85, names(cm$byClass[2]), cex=1.2, font=2)
  text(30, 70, round(as.numeric(cm$byClass[2]), 3), cex=1.2)
  text(50, 85, names(cm$byClass[5]), cex=1.2, font=2)
  text(50, 70, round(as.numeric(cm$byClass[5]), 3), cex=1.2)
  text(70, 85, names(cm$byClass[6]), cex=1.2, font=2)
  text(70, 70, round(as.numeric(cm$byClass[6]), 3), cex=1.2)
  text(90, 85, names(cm$byClass[7]), cex=1.2, font=2)
  text(90, 70, round(as.numeric(cm$byClass[7]), 3), cex=1.2)
  
  # add in the accuracy information 
  text(30, 35, names(cm$overall[1]), cex=1.5, font=2)
  text(30, 20, round(as.numeric(cm$overall[1]), 3), cex=1.4)
  text(70, 35, names(cm$overall[2]), cex=1.5, font=2)
  text(70, 20, round(as.numeric(cm$overall[2]), 3), cex=1.4)
}  

#heat map functions 
#from #http://www.sthda.com/english/wiki/ggplot2-quick-correlation-matrix-heatmap-r-software-and-data-visualization
get_lower_tri<-function(cormat){
  cormat[upper.tri(cormat)] <- NA
  return(cormat)
}
# Get upper triangle of the correlation matrix
get_upper_tri <- function(cormat){
  cormat[lower.tri(cormat)]<- NA
  return(cormat)
}


#' Makes the three EDA plots
#'
#' @param X_train_path 
#' @param y_train_path 
#'
#' @export 
#' img/01_corr_heatmap.png
#' img/02_confusion_matrix.png
#' img/03_prop_result.png
#' 
main <- function(X_train_path, y_train_path) {
  
  test_that("The X_train_path and y_train_path is correct", {
    expect_equivalent(X_train_path, "data/clean-data/Xtrain-clean-autism-screening.csv")
    expect_equivalent(y_train_path, "data/clean-data/ytrain-clean-autism-screening.csv")
    
  })

  #read files
  df_autism_X <- read_csv(X_train_path)
  df_autism_y <- read_csv(y_train_path)
  
  #clean and name df
  df_autism_y$X1 <- NULL
  df_autism <- cbind(df_autism_X, df_autism_y)
  names(df_autism) <- make.names(names(df_autism))
  
  df_autism$gender <- as.factor(df_autism$gender)
  df_autism$jaundice <- as.factor(df_autism$jaundice)
  df_autism$autism <- as.factor(df_autism$autism)
  df_autism$Class.ASD <- tolower(df_autism[[21]])
  df_autism$Class.ASD <- as.factor(df_autism$Class.ASD)
  
  a_score <- c('A1_Score', 'A2_Score', 'A3_Score', 'A4_Score', 'A5_Score', 'A6_Score', 'A7_Score', 'A8_Score', 'A9_Score', 'A10_Score')
  
  #plot 1 heat map
  
  cormat <- df_autism  %>% 
    select(a_score)  %>% 
    cor()
  
  melted_cormat <- melt(cormat)
  
  upper_tri <- get_lower_tri(cormat)
  melted_cormat <- melt(upper_tri, na.rm = TRUE) %>% 
    filter(value < 1)
  
  corr_heatmap <- ggplot(melted_cormat, aes(x=Var1, y=Var2, fill = value))+
    geom_tile()+
    ggtitle("Correlation Heatmap")+
    labs(fill = "Correlation")+
    theme(axis.title.x=element_blank(),
          axis.ticks.x=element_blank(),
          axis.title.y=element_blank(),
          axis.ticks.y=element_blank(),
          legend.justification = c(1, 0),
          legend.position = c(0.6, 0.7),
          legend.direction = "horizontal",
          panel.border = element_blank(), panel.grid.major = element_blank(),
          panel.grid.minor = element_blank(), axis.line = element_line(colour = "black"))+
    guides(fill = guide_colorbar(barwidth = 7, barheight = 1,
                                 title.position = "top", title.hjust = 0.5))
  
  
  ggsave(plot = corr_heatmap, "img/01_corr_heatmap.png", width = 8, height = 5)
  
  #plot 2 confusion matrix 
  numLlvs <- 2
  cm <- confusionMatrix(
    df_autism$autism,
    df_autism$Class.ASD)  
  
  plot <- draw_confusion_matrix(cm)
  ggsave(plot = draw_confusion_matrix(cm), "img/02_confusion_matrix.png",width = 7, height = 5)
  
  #plot 3 bar chart
  df_autism  %>% 
    ggplot()+
    geom_bar(mapping = aes(x=as.factor(result), fill = autism),
             position = "fill")+
    ylab("Proportion of Participants")+
    xlab("ASD-10 Test Score")+
    ggtitle("Proportion of Participants by ASD-10 Test Score")+
    scale_fill_brewer(name = "Diagnosed \nwith Autism", palette = "Paired")+
    theme(panel.border = element_blank(), panel.grid.major = element_blank(),
          panel.grid.minor = element_blank(), axis.line = element_line(colour = "black"))
  
  ggsave("img/03_prop_result.png", width = 7, height = 5)
  
}


x_train <- "../data/clean-data/Xtrain-clean-autism-screening.csv"
y_train <- "../data/clean-data/ytrain-clean-autism-screening.csv"

main(opt[["--X_train_path"]], opt[["--y_train_path"]])



