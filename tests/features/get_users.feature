Feature: Get posts from JsonPlaceholder API
  In order to view its content
  As a reader
  I want to retrieve posts

  Scenario: Get all posts
     Given API service is running
      When retrieving posts
      Then list of posts is not empty

  Scenario Outline: Get post with ID <id>
   Given API service is running
    When retrieving post with ID <id>
    Then only post with ID <id> is retrieved
    Examples: Post IDs
    | id  |
    | 1 |
    | 2 |
    | 3 |