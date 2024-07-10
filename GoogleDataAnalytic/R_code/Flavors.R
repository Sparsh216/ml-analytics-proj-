library(tidyverse)
flavors_df=read.csv('C:\\Users\\krish\\OneDrive\\Desktop\\flavors_of_cacao.csv')
view(flavors_df)

glimpse(flavors_df)

new_flavors=flavors_df %>% 
  rename(Maker=CompanyÂ...Maker.if.known.)
view(new_flavors)

trimmed_flavors_df=flavors_df %>% select(Rating,Cocoa.Percent,CompanyÂ...Maker.if.known.,Company.Location)

trimmed_flavors_df %>% summarise(mean(Rating))

best_trimmed_flavors_df=trimmed_flavors_df %>% filter(Cocoa.Percent>=75&Rating>=3.9&Company.Location)

ggplot(data=trimmed_flavors_df)+geom_bar(mapping = aes(y=Cocoa.Percent))
                                              