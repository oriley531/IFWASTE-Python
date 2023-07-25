library(tidyverse)
library(ggplot2)
library (gridExtra)
library(cowplot)
library(ineq)
library(gglorenz)
library(hrbrthemes)


hh_foodwasted <- read.csv("C:/PythonCodes/IFWASTE-Python-Restructured/IFWASTE-Python-Restructured/wasted_food1.csv")
hh_foodbought <- read.csv("C:/PythonCodes/IFWASTE-Python-Restructured/IFWASTE-Python-Restructured/bought_food_1.csv")



ggplot(hh_foodwasted,aes(x=Type,y=kg,group=House)) + geom_boxplot()+ggtitle("Wasted Food") + ylab("Kg Wasted")+ xlab("Food Category")+theme_bw()
ggplot(hh_foodbought,aes(x=Day.Bought,y=Price,group=House)) + geom_boxplot()+ggtitle("Food Bought") + ylab("Price")+ xlab("Time")+theme_bw()


#Energy Rainbow Graphs
fnvbought <- filter(hh_foodbought,Type=="Fruits & Vegetables")
hh1_only<- filter(hh_foodbought,House==1)
hh2_only<- filter(hh_foodbought,House==2)

ggplot()+ggtitle("Fruits & Veg") +geom_line(data=fnvbought,aes(x=Day.Bought,y=Price,group=House,colour = House), alpha = 0.4, size = 2)+ geom_line()+labs(y= "Fruits&Veg Bought (kg)", x = "Month") + scale_color_gradientn(colours = rainbow(20))+ ylim(0, 25)


#Stacked Bar

fill <- c("darkgrey","tan2","forestgreen","red","yellow")
leglabels <- c("Dairy & Eggs", "Dry Foods & Baked Goods","Fruits & Vegetables","Meat& Fish",
               "Snacks, Condiments, Liquids, Oils, Grease, & Other")

hh1_buy <- ggplot()+ggtitle("HH #1 Food Kg Purchased")+labs(y= "Food Purchased (kg)", x = "Simuated Days") + geom_bar(aes(y = kg, x = Day.Bought, fill = Type), data = hh1_only, stat="identity") +
  scale_fill_manual(values = fill) + theme(legend.position="none")+theme_bw()
hh1_buy

hh2_buy <- ggplot()+ggtitle("HH #2 Food Kg Purchased")+labs(y= "Food Purchased (kg)", x = "Simuated Days") + geom_bar(aes(y = kg, x = Day.Bought, fill = Type), data = hh2_only, stat="identity") +
  scale_fill_manual(values = fill) + theme(legend.position="none")+theme_bw()
hh2_buy

