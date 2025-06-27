# Created by sergiovillar at 6/17/25
Feature: Tests for Target




  Scenario: verify that a logged out user can navigate to Sign In
    Given open target main page
    When selecting account and clicking sign in
    Then Verify that sign in page opens