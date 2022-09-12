Examples
=============


How to get account balance?
------------------------------


.. code-block:: python

    import asyncio

    from aioproxyline import ProxyLine

    async def get_balance(api_token: str) -> None:
        async with ProxyLine(api_token=api_token) as client:
            result = await client.get_balance()  # Balance(balance=0.0, partner_balance=0.0)


    asyncio.run(get_balance(api_token='my_token'))

How to get proxy list?
---------------------------------


.. code-block:: python

    import asyncio

    from aioproxyline import ProxyLine

    async def get_proxies(api_token: str) -> None:
        async with ProxyLine(api_token=api_token) as client:
            proxies = await client.get_proxies()



    asyncio.run(get_proxies(api_token='my_token'))

How to get my orders?
-----------------------


.. code-block:: python

    import asyncio

    from aioproxyline import ProxyLine

    async def get_orders(api_token: str) -> None:
        async with ProxyLine(api_token=api_token) as client:
            orders = await client.get_orders()



    asyncio.run(get_orders(api_token='my_token'))


How to renew proxy?
--------------------------------


.. code-block:: python

    import asyncio

    from aioproxyline import ProxyLine

    async def renew_proxy(api_token: str, proxy_id: int, period: int) -> None:
        async with ProxyLine(api_token=api_token) as client:
            await client.renew_proxy(proxy=proxy_id, period=period)



    asyncio.run(renew_proxy(api_token='my_token', operation_id=551166)

How to order proxy?
----------------------------


.. code-block:: python

    import asyncio

    from aioproxyline import ProxyLine
    from aioproxyline.types import ProxyType, ProxyProtocol

    async def order_proxy(api_token: str) -> None:
        async with ProxyLine(api_token=api_token) as client:
            proxy = await client.order_proxy(proxy_type=ProxyType.DEDICATED,
                                             ip_version=ProxyProtocol.IPv4, country="ru",
                                             period=30)



    asyncio.run(order_proxy(api_token='my_token')

How to get order price?
--------------------------------


.. code-block:: python

    import asyncio

    from aioproxyline import ProxyLine
    from aioproxyline.types import ProxyType, ProxyProtocol

    async def get_order_price(api_token: str) -> None:
        async with ProxyLine(api_token=api_token) as client:
            proxy = await client.get_order_price(proxy_type=ProxyType.DEDICATED,
                                                 ip_version=ProxyProtocol.IPv4, country="ru",
                                                 period=30, quantity=1)
            print(proxy) # price=1.77 data=PriceData(ip_list=[], period=30, country='ru', type=<ProxyType.DEDICATED: 'dedicated'>, ip_version=<ProxyProtocol.IP_V4: 4>, quantity=1)




    asyncio.run(get_order_price(api_token='my_token')

How to get available countries with cities?
---------------------------------------------


.. code-block:: python

    import asyncio

    from aioproxyline import ProxyLine

    async def get_countries(api_token: str) -> None:
        async with ProxyLine(api_token=api_token) as client:
            countries = await client.get_countries()
            print(countries) # [Countries(code='ru', name='Russia', cities=[Cities(id=29, name='Astrakhan'), Cities(id=64, name='Belgorod')





    asyncio.run(get_countries(api_token='my_token')

How to get IPs?
----------------------------


.. code-block:: python

    import asyncio

    from aioproxyline import ProxyLine
    from aioproxyline.types import ProxyType, ProxyProtocol

    async def get_ips(api_token: str) -> None:
        async with ProxyLine(api_token=api_token) as client:
            ips = await client.get_ips(ProxyType.DEDICATED, ProxyProtocol.IP_V4, country='ru')
            print(ips) # [IPs(id=10271, ip='45.149.*.*'), IPs(id=14428, ip='45.156.*.*'), IPs(id=14527, ip='45.153.*.*'), ...]





    asyncio.run(get_ips(api_token='my_token')

How to get IPs count?
-----------------------------


.. code-block:: python

    import asyncio

    from aioproxyline import ProxyLine
    from aioproxyline.types import ProxyType, ProxyProtocol

    async def get_ips_count(api_token: str) -> None:
        async with ProxyLine(api_token=api_token) as client:
            ips = await client.get_ips_count(ProxyType.DEDICATED, ProxyProtocol.IP_V4, country='ru')
            print(ips.count) # 1000





    asyncio.run(get_ips(api_token='my_token')