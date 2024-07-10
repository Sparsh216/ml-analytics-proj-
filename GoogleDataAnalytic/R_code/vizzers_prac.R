library(ggplot2)
library(palmerpenguins)
data("penguins")
View(penguins)

ggplot(data = penguins)+geom_point(mapping= aes(x=flipper_length_mm,y=body_mass_g))
ggplot(data = penguins)+geom_col(mapping= aes(x=flipper_length_mm,y=body_mass_g))
library(ggplot2)
ggplot(data=bookings_df)+geom_point(mapping = aes(x=stays_in_weekend_nights,y=children))

ggplot(data=bookings_df)+geom_bar(mapping=aes(x=distribution_channel))+facet_grid(~deposit_type~market_segment)+theme(axis.text = element_text(angle = 45))

ggplot(data=bookings_df)+geom_bar(mapping = aes(x=hotel))+facet_wrap(~market_segment)

library(tidyverse)
onlineta_city_hotels=filter(bookings_df,(hotel=="City Hotel" & bookings_df$market_segment=="Online TA"))

view(onlineta_city_hotels)
ggplot(data = onlineta_city_hotels)+geom_point(mapping = aes(x=lead_time,y=children))

mindate=min(bookings_df$arrival_date_year)
maxdate=max(bookings_df$arrival_date_year)
ggplot(data = bookings_df)+geom_bar(mapping = aes(x=market_segment))+facet_wrap(~hotel)+theme(axis.text.x=element_text(angle=45))+labs(title="Count vs Market_Segment",caption = paste0("data from: ",mindate, " to ",maxdate))
