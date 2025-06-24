# Created by sergiovillar at 6/19/25
Feature: Cart tests

  Scenario: User clicks on the cart icon and verifies that “Your cart is empty” message is shown.
    Given open target main page
    When click on cart
    Then Verify that “Your cart is empty” message is shown.


  Scenario: User adds product to cart and verifies it's in the cart
    Given open target main page
    When Search for body wash
    Then add body wash to the cart
    And add body wash to cart on options menu
    And verify body wash was added to cart
    And Verify cart has 1 item(s)