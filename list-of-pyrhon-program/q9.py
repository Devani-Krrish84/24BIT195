def rs_to_dollars(rs):
    return rs / 48

# Example usage
rs = float(input("Enter the amount in Rs.: "))
print(f"{rs} Rs. is equal to {rs_to_dollars(rs)} dollars.")