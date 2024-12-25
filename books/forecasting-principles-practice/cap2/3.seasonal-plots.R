PBS |>
    filter(ATC2 == "A10") |>
    select(Month, Concession, Type, Cost) |>
    summarise(TotalC = sum(Cost)) |>
    mutate(Cost = TotalC/1e6) -> a10

autoplot(a10, Cost)

# seasonal plot
a10 |> 
    gg_season(Cost, labels="both") +
    labs(y="$ (millions)",
    title = "Seasonal plot") -> plot



# Multiple seasonal plot

filtered_data <- vic_elec |>
    filter(year(Time)==2013 & month(Time)==1)
## Amostra mensal
autoplot(filtered_data, Demand)


# é possível observar um padrão sazonal diário
vic_elec |> gg_season(Demand, period = "week") +
  theme(legend.position = "none") +
  labs(y="MWh", title="Electricity demand: Victoria") -> plot2