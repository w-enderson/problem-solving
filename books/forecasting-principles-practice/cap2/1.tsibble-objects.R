library("tsibble")
library("fpp3")

# transformar em tsibble object
y <- tsibble(
  Year = 2015:2019,
  Observation = c(123, 39, 78, 52, 110),
  index = Year
)

print(y) 



####
# categorias de cada variável (há 14 séries temporais)
# variável índice = coluna temporal; chaves = demais;

print(olympic_running) 

print( olympic_running |> distinct(Sex) )
print( olympic_running |> distinct(Length) )



####
# Trabalhando com tsibble objects

print(PBS)

# seleciona linhas particulares;
# seleciona colunas particulares;
# soma o custo de todas as linhas com mesmo (Month, Conscession, Type)
# cria variáveis
PBS |>
    filter(ATC2 == "A10") |>
    select(Month, Concession, Type, Cost) |>
    summarise(TotalC = sum(Cost)) |>
    mutate(Cost = TotalC/1e6) -> a10



####
# CSV to tsibble

prison <- readr::read_csv("https://OTexts.com/fpp3/extrafiles/prison_population.csv")


prison <- prison |>
    mutate(Quarter = yearquarter(Date)) |> # trimestre
    select(-Date) |> 
    as_tsibble(key=c(State, Gender, Legal, Indigenous),
        index = Quarter)
        
print(prison)

