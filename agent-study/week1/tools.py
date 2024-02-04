tools = [
    {
        "name": "get_url_from_query",
        "description": "get url from user query",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "user query",
                },
            },
        },
    },
    {
        "name": "get_product_price",
        "description": "user want to get product price from user query.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "user query",
                },
                "name": {
                    "type": "string",
                    "description": "product name",
                },
            },
            "required": ["query", "name"],
        },
    },
    {
        "name": "get_information_from_query",
        "description": "user want to get product information from user query.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "user query",
                },
            },
            "required": ["query"],
        },
    },
]