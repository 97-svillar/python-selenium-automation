Feature: Tests for Target Search

  Scenario: User can search for tea
    Given Open target main page
    When Search for tea
    Then Verify search worked for tea

  Scenario: User can search for a mug on Target
    Given Open target main page
    When Search for mug
    Then Verify search worked for mug

  Scenario: User can search for coffee on Target
    Given Open target main page
    When Search for coffee
    Then Verify search worked for coffee

  Scenario Outline: User can search for a product
    Given Open target main page
    When Search for <search_word>
    Then Verify search worked for <expected_result>
    Examples:
    | search_word | expected_result |
    | tea         |tea              |
    | mug         |mug              |
    | coffee      |coffee           |

    Scenario: User can see favorites tooltip for search results
    Given Open Target main page
    When Search for tea
    And Hover favorites icon
    Then Favorites tooltip is shown