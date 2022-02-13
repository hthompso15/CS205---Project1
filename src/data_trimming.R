# CS 205 
# Group 10
# Warmup

# Imports
library(tidyverse)
library(dplyr)
library(lubridate)

# Hard Coded set working directory for printing ease
# NEEDS to be changed for anyone else to run
setwd("~/Desktop/CS 205/group10-warmup")

# Chosen Variables for each File 

# Population File
# Country 
# Population
# Urban Population
# Percentage of Global

# GDP File
# Country
# Population
# Urban Population
# World Share

# Read in Data files
pop20 <- read.csv("../data/pop2020.csv")
gdp <- read.csv("../data/gdp_1960_2020.csv",stringsAsFactors = FALSE)

# Data Filtering and Cleaning
gdp20 <- gdp %>% filter(year == "2020", country != "Columbia", country != "Hong Kong", country != "Singapore", rank <= 40) %>% select(country,gdp_percent,gdp,rank)

gdp20[1,"country"] <- "United States"

pop20 <- pop20 %>% select(Country..or.dependency.,Population..2020.,Urban.Pop..,World.Share) 

pop20 %>% filter(gdp20$country %in% pop20$Country..or.dependency.)

pop20 <- pop20 %>% mutate(yes = ifelse(pop20$Country..or.dependency. %in%  gdp20$country, "yes","no"))

pop20 <-  pop20 %>% filter(yes == "yes", Country..or.dependency. != "Hong Kong", Country..or.dependency. != "Singapore")

pop20 <- pop20 %>% select(Country..or.dependency.,Population..2020.,Urban.Pop..,World.Share) 



# Write to csv file
write.csv(gdp20,"../data/gdp2020.csv", row.names = TRUE)

write.csv(pop20,"../data/pop2020.csv", row.names = TRUE)







