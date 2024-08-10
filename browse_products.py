def browse_amazon(product_name, max_price):
    from multion.client import MultiOn
    import time

    client = MultiOn(api_key="105ae8bf8848469e9fdf0efcba4c9688")

    browse_cmd = "Find the product " + product_name + " and add it to my Amazon cart if the price is less than " + max_price + "."

    browse_session = client.sessions.create(
        url="https://www.amazon.com/",
        local=True,
        use_proxy=True
    )
    session_id = browse_session.session_id

    status = "CONTINUE"
    while status == "CONTINUE":
        step_response = client.sessions.step(
            session_id=session_id,
            cmd=browse_cmd
        )
        status = step_response.status

    time.sleep(30)
    client.sessions.close(
        session_id=session_id
    )

