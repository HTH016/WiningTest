def calc(
    user: str,
    product_infos: list,
    quantity_per_ones: list,
    price_per_ones: list,
    current_time: str,
    user_point: int,
    all_price: int,
    cart_info: str = None,
) -> dict or None:
    """
    매개변수로 입력 받은 값을 연산을 해서 데이터를 반환해주는 함수입니다
    """
    print("calcurating...")
    _quantity_all = 0

    for i in range(len(price_per_ones)):
        _quantity_all += int(quantity_per_ones[i])
    if int(user_point) >= int(all_price):
        user_point = int(user_point) - int(all_price)

        result = {
            "user": user,
            "quantity_all": _quantity_all,
            "price_all": all_price,
            "current_time": current_time,
            "product_infos": product_infos,
            "quantity_per_ones": quantity_per_ones,
            "price_per_ones": price_per_ones,
            "user_point": user_point,
        }

        if cart_info != None:
            result["cart_info"] = cart_info
            print("product_info: ", type(result["product_infos"]))

    else:
        result = None

    return result


def formating(
    user: str,
    product_info: str,
    quantity: int,
    price_per_one: int,
    wine_name: str,
    wine_image: str,
    identifier: str = None,
) -> dict:
    dto = {
        "user": user,
        "identifier": identifier,
        "product_info": product_info,
        "quantity": quantity,
        "price_per_one": price_per_one,
        "purchase_price": int(price_per_one) * int(quantity),
        "wine_image": wine_image,
        "wine_name": wine_name,
    }
    return dto
