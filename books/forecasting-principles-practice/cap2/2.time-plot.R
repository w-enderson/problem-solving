library("tsibble")
library("fpp3")


melsyd_economy <- ansett |>
    filter(Airports == "MEL-SYD", Class=="Economy") |>
    mutate(Passengers=Passengers/1000) |>
    mutate(Week = as.Date(Week))


autoplot(melsyd_economy, Passengers) + 
    labs(title="Ansett airlines economy class",
    subtitle="Melbourne-Sydney",
    y = "Passengers ('000')"
) +
    scale_x_date(
        date_breaks = "52 week", 
        date_labels = "%d %b %Y"
    )-> a

print(ansett)
print(a)


