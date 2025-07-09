# Created by sergiovillar at 7/9/25
Feature: Tests for Help pages

  Scenario: User can select Help topic Promotions & Coupons
    Given Open Help page for Returns
    Then Verify help Returns page opened
    When Select Help topic Promotions & Coupons
    Then Verify help Current promotions page opened

  Scenario: User can select Help topic Target Circle™
    Given Open Help page for Returns
    Then Verify help Returns page opened
    When Select Help topic Target Circle™
    Then Verify help About Target Circle page opened

  Scenario: User can select Help Topics Compliance
    Given Open Help page for Returns
    Then Verify help Returns page opened
    When Select Help topic Compliance
    Then Verify help Baby & Toddler Food page opened
