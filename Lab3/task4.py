"""
Task 4) Product Data Transformer (lambda, map, filter, zip)
   - Ask user for a list of product names (comma-separated).
   - Ask user for a list of product prices (comma-separated).
   - Process them by:
        - Pairing product with price.
        - Filtering out items where price <= 0.
        - Transforming each pair into a dictionary {"product": name, "price": price, "discounted": price * 0.9}.
   - Save the final result as JSON into "products.json".
   - Print a preview of the first 5 results.
"""
import json

def transformer():
    try:
        product_names = list(map(str.strip, input("Enter product names: ").split(",")))
        product_prices = list(map(float, input("Enter product prices: ").split(",")))

        if len(product_names) != len(product_prices):
            print("The number of product names and prices must be the same.")
            return
        paired = zip(product_names, product_prices)

        filtered = filter(lambda x: x[1] > 0, paired)
        transformed = list(map(lambda x: {"product": x[0], "price": x[1], "discounted": x[1] * 0.9}, filtered))

        with open("products.json", "w") as json_file:
            json.dump(transformed, json_file, indent=4)
    except ValueError:
        print("Invalid input. Please enter numeric values for prices.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return