Feature: Booking search
    A search engine where you can find a hotel that meets your needs.

Background:
    Given I am at https://www.rocketmiles.com/

Scenario: Default search parameters
    When I click the search button
    Then the search should not be performed
    And the "Unknown location" error should appear