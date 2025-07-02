# Created by sergiovillar at 6/17/25
Feature: Tests for Target Sign-in




  Scenario: verify that a logged out user can navigate to Sign In
    Given open target main page
    When selecting account and clicking sign in
    Then Verify that sign in page opens

  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open sign in page
    When Store original window
    And Click on Target terms and conditions link
    And Switch to new window
    Then Verify Terms and Conditions page is opened
    And User can close new window and switch back to original
