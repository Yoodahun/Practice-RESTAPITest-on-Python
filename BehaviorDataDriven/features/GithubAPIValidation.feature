# Created by yoodahun at 2020/11/23
Feature: Github API Validation
  # Enter feature description here

  Scenario: Session management check
   Given I have github auth credential
    When I hit getRepo API of github
    Then status code of response should be 200
