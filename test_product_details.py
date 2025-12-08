from product_details import product_details

def test_product_details():
    expected_output = (
        "Product ID: 101\n"
        "Product Name: iPhone\n"
        "Quantity: 1\n"
        "Price: 155000"
    )

    assert product_details(101, "iPhone", 1, 155000) == expected_output
