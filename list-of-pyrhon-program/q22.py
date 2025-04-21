def calculate_net_sales(gross_sales):
    discount = gross_sales * 0.1
    return gross_sales - discount

# Example usage
gross_sales = float(input("Enter the gross sales: "))
net_sales = calculate_net_sales(gross_sales)
print(f"The net sales are: {net_sales}")