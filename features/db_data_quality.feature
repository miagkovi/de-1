Feature: Validate data integrity in database

  Scenario: No duplicate CPU names exist in database after load
    When I query the database for duplicate cpu_name values
    Then there should be no duplicate cpu_name values in the database

  Scenario: All CPU prices are greater than zero
    When I query the database for invalid price values
    Then all prices should be greater than zero
