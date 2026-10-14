# Reporte de Análisis de Datos - Pandas

`Alexandro Aguilar Machine Learning pandas, NC 0007`

## 1. DataFrame Convertido
```text
  Nombre  Edad  Salario
0   Luis    28    15000
1  Elena    34    18000
2  Pedro    45    22000
3   Rosa    29    16000
4  Jorge    38    20000
5  Marta    52    25000
```

## 2.1 Primeras Filas (head)
```text
  Nombre  Edad  Salario
0   Luis    28    15000
1  Elena    34    18000
```

## 2.2 Últimas Filas (tail)
```text
  Nombre  Edad  Salario
4  Jorge    38    20000
5  Marta    52    25000
```

## 2.3 Dimensiones (Filas, Columnas)
```text
(6, 3)
```

## 2.4 Tipos de Datos por Columna
```text
Nombre       str
Edad       int64
Salario    int64
dtype: object
```

## 2.5 Información General (info)
```text
<class 'pandas.DataFrame'>
RangeIndex: 6 entries, 0 to 5
Data columns (total 3 columns):
 #   Column   Non-Null Count  Dtype
---  ------   --------------  -----
 0   Nombre   6 non-null      str  
 1   Edad     6 non-null      int64
 2   Salario  6 non-null      int64
dtypes: int64(2), str(1)
memory usage: 276.0 bytes

```

## 3. Estadísticas Generales de la Columna 'Salario'
```text
count        6.000000
mean     19333.333333
std       3777.124126
min      15000.000000
25%      16500.000000
50%      19000.000000
75%      21500.000000
max      25000.000000
Name: Salario, dtype: float64
```

## 4. Ordenar Ascendente por Salario
```text
  Nombre  Edad  Salario
0   Luis    28    15000
3   Rosa    29    16000
1  Elena    34    18000
4  Jorge    38    20000
2  Pedro    45    22000
5  Marta    52    25000
```

## 5. Ordenar Descendente por Edad
```text
  Nombre  Edad  Salario
5  Marta    52    25000
2  Pedro    45    22000
4  Jorge    38    20000
1  Elena    34    18000
3   Rosa    29    16000
0   Luis    28    15000
```

`Alexandro Aguilar Machine Learning pandas, NC 0007`