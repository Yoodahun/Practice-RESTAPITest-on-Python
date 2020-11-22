# Created by yoodahun at 2020/11/22

Feature: Verify if Books are added and deleted using Library API
  # Enter feature description here

  Scenario: Verify AddBook API functionality
    # Enter steps here
    Given the Book details which needs to be added to Library
    When We execute the AddBook PostAPI method
    Then book is successfully added
