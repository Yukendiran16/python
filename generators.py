# import datetime
#
# brand_name = ["Apple", "Sony", "Samsung", "Vivo", "Redmi", "Realme"]
# price = ["90K", "40K", "30K", "25K", "20K", "18K"]
#
# stock_list = ["Amazon", "Google", "SpaceX", "Tesla", "FlipCart", "MicroSoft", "PhonePay", "Paytm", "Paypal", "Tata"]
# old_stock = [4456.543, 6434.554, 5354.453, 4536.435, 6356.455, 4335.453, 3523.252, 5252, 2645, 5422]
#
#
# def get_warnings(log_file):
#     for log_row in open(log_file):
#         if 'WARN' in log_row:
#             yield log_row
#
#
# def product_list(brands_count):
#     for product_id in range(brands_count):
#         product = {
#             "id": product_id,
#             "Brand_name": brand_name[product_id],
#             "Price": price[product_id]
#         }
#         yield product
#
#
# def stocks(n):
#     for stock in range(n):
#         stock_money = {
#             "stock_name": stock_list[stock],
#             "stock_price": round(old_stock[stock] + old_stock[stock] % 1000 * 1.5, 3)
#         }
#         yield stock_money
#
#
# def armstrong_number(n):
#     for i in range(n):
#         result = 0
#         new_value = i
#         while i > 0:
#             rem = i % 10
#             result += rem ** 3
#             i //= 10
#         if result == new_value:
#             yield result
#         else:
#             continue
#;
#
# for warning_line in get_warnings('C:/Users/lenovo/Downloads/app.log'):
#     print(warning_line)
#
# print("\n")
#
# for brand in product_list(len(brand_name)):
#     print(brand)
#
# print("\n")
#
# for stock_price in stocks(len(stock_list)):
#     print(stock_price)
#
# print("\n")
#
# print("Enter a number for find armstrong series")
# for value in armstrong_number(int(input())):
#     print(value)


def generate():
    for i in [1,2,3,4,5]:
        print(i)
        result = "I2I" + str(i)
        print('first: ', result)
        yield result
        print("end")


ids = generate()
while True:
    print(ids)
    generate_id = input("Generate Id yes/no")
    if generate_id == "yes":
        print('final: ', next(ids))
    else:
        break

