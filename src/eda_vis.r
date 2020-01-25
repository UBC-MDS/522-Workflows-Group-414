#load packages
library(tidyverse)
library(reshape2)
library(docopt)
library(caret)
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
  rect(150, 430, 240, 370, col='#3F97D0')
  text(195, 435, 'ASD Diagnosed', cex=1.2)
  rect(250, 430, 340, 370, col='#F7AD50')
  text(295, 435, 'ASD-10 Result', cex=1.2)
  text(125, 370, 'Predicted', cex=1.3, srt=90, font=2)
  text(245, 450, 'Actual', cex=1.3, font=2)
  rect(150, 305, 240, 365, col='#F7AD50')
  rect(250, 305, 340, 365, col='#3F97D0')
  text(140, 400, 'ASD Diagnosed', cex=1.2, srt=90)
  text(140, 335, 'ASD-10 Result', cex=1.2, srt=90)
  
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


main <- function(X_train_path, y_train_path) {
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
  
  corr_heatmap <- df_autism  %>% 
    select(a_score)  %>% 
    cor() %>% 
    melt() %>% 
    filter(value < 1) %>% 
    ggplot(aes(x=Var1, y=Var2, fill = value))+
    geom_tile()+
    ggtitle("Correlation Heatmap")+
    xlab("Predictor")+
    ylab("Predictor")+
    labs(fill = "CORR")
  
  corr_heatmap
  
  ggsave("img/01_corr_heatmap.png", width = 8, height = 5)
  
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
             position = "fill")
  
  ggsave("img/03_prop_result.png", width = 7, height = 5)
  
}


x_train <- "../data/clean-data/Xtrain-clean-autism-screening.csv"
y_train <- "../data/clean-data/ytrain-clean-autism-screening.csv"

main(opt[["--X_train_path"]], opt[["--y_train_path"]])



