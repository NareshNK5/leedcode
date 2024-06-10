import pandas as pd
def find_products(products: pd.DataFrame) -> pd.DataFrame:
    print(products)
    filtered_products = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    result = pd.DataFrame(filtered_products['product_id'])
    print(result,type(products))
products = pd.read_csv("1757. Recyclable and Low Fat Products.csv")
products = pd.DataFrame(products)
find_products(products)

'''
import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    table = products[(products.low_fats == 'Y')&(products.recyclable == 'Y')]
    return table[['product_id']]
'''