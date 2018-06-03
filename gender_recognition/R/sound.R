setwd("/home/gavy42/Desktop/github/MozartFlow/gender_recognition/R")

#packages <- c('tuneR', 'seewave', 'fftw', 'caTools', 'randomForest', 'warbleR', 'mice', 'e1071', 'rpart', 'rpart-plot', 'xgboost', 'e1071')
#if (length(setdiff(packages, rownames(installed.packages()))) > 0) {
#  install.packages(setdiff(packages, rownames(installed.packages())))  
library(warbleR)
require(warbleR)

processFolder <- function(folderName) {
  # Start with empty data.frame.
  data <- data.frame()
  # Get list of files in the folder.
  list <- list.files(folderName)
  # Add file list to data.frame for processing.
  for (fileName in list) {
    row <- data.frame(fileName, 0, 0, 20)
    data <- rbind(data, row)
  }
  # Set column names.
  names(data) <- c('sound.files', 'selec', 'start', 'end')
  # Move into folder for processing.
  setwd(folderName)
  
  acoustics <- specan3(data, parallel=1)
  setwd('..')
  return(acoustics)
}

test <- processFolder('test')

test$duration <- NULL
test$sound.files <- NULL
test$selec <- NULL
test$peakf <- NULL

test <- test[complete.cases(test),]
write.csv(test, file='voicetest.csv', sep=',', row.names=F)
