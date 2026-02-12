#!/usr/bin/env python3

for table_num in range(1, 11):
    print(f"Table de {table_num}:", end=" ")
        
    for multiplier in range(0, 11):
        result = table_num * multiplier
        print(f"{result}", end="  ")
        
    print("")