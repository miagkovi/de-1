from behave import when, then


@when("I query the database for duplicate cpu_name values")
def step_query_duplicates(context):
    query = """
        SELECT COUNT(*)
        FROM (
            SELECT cpu_name
            FROM cpu
            GROUP BY cpu_name
            HAVING COUNT(*) > 1
        ) sub;
    """

    with context.conn.cursor() as cur:
        cur.execute(query)
        context.duplicate_count = cur.fetchone()[0]


@then("there should be no duplicate cpu_name values in the database")
def step_assert_no_duplicates(context):
    assert context.duplicate_count == 0, (
        f"Found {context.duplicate_count} duplicated cpu_name values"
    )


@when("I query the database for invalid price values")
def step_query_invalid_prices(context):
    query = """
        SELECT COUNT(*)
        FROM cpu
        WHERE price <= 0 OR price IS NULL;
    """

    with context.conn.cursor() as cur:
        cur.execute(query)
        context.invalid_price_count = cur.fetchone()[0]


@then("all prices should be greater than zero")
def step_assert_prices(context):
    assert context.invalid_price_count == 0, (
        f"Found {context.invalid_price_count} invalid price values"
    )
