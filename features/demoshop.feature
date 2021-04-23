Feature: DemoShop Study Case

  Scenario: DemoShop - Search
    Given i create a url <http://demoshop24.com/>
    Then i visit to url
    Then i search <Macbook>
    And i assert <3> products has exist
    And i assert all search products name contains <MacBook>


  Scenario: DemoShop - Add Cart
    Given i create a url <http://demoshop24.com/>
    Then i visit to url
    Then i search <Macbook>
    And i assert <3> products has exist
    Then i add first product to cart
    And i assert cart has <1 item>

  Scenario: DemoShop - Login
    Given i create a url <http://www.demoshop24.com/index.php?route=account/register>
    Then i visit to url
    Then i fill form
      | FIELD            | VALUE              |
      | First Name       | Baris              |
      | Last Name        | Ozdicle            |
      | E-Mail           | demoshop2@test.com |
      | Telephone        | 123456789          |
      | Password         | Pwd123             |
      | Password Confirm | Pwd123             |
    And i accept Privacy Policy
    And i click to Continue
    And i assert <Your Account Has Been Created!> message has exist on page title
