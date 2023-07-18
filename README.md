<h1 align="center"> Airbnb Clone Project </h1>

<img src="./images/65f4a1dd9c51265f49d0.png">

## About it

This is an AirBnB clone project developed as part of the Holberton School curriculum. It aims to replicate the core functionality of the AirBnB website and provide a command-line interface to interact with the application.

## Description

The AirBnB Clone project consists of developing a simplified version of the AirBnB website. It includes the implementation of various classes and functionalities such as creating and managing user accounts, handling properties and rentals, managing amenities and reviews, and more.

## Command Interpreter

The Command Interpreter, also known as the console, is a key component of the AirBnB Clone project. It provides a command-line interface for users to interact with the application and perform various operations, such as creating and managing instances, querying data, and updating objects.

## Features

- **Create**: Create new instances of different classes available in the application, such as User, Property, Review, and more. Specify the attributes of the instance during creation.

- **Show**: View the details of a specific instance by providing its class name and ID. The Command Interpreter displays the string representation of the instance, including its attributes.

- **Destroy**: Delete an instance by specifying its class name and ID. Once deleted, the instance and its associated data will be removed from the application.

- **All**: View all instances of a specific class or all instances available in the application. The Command Interpreter retrieves the instances from the data storage and displays their string representations.

- **Update**: Update the attributes of an instance by specifying its class name, ID, attribute name, and new value. The Command Interpreter modifies the instance's attribute and saves the changes to the data storage.

- **Quit**: Exit the Command Interpreter and terminate the application.

## Installation

To use the Holberton School AirBnB Clone project, follow these steps:

1. Clone the repository from GitHub:

`$ git clone https://github.com/IsmaelMolina-code/holbertonschool-AirBnB_clone.git`

2. Navigate to the project directory:

`$ cd holbertonschool-AirBnB_clone`

3. Run the console by writting: python ./console.py or just ./console.py

4. Once the Command Interpreter is running, you can start using the available commands to interact with the application. Refer to the project's documentation or use the `help` command within the Command Interpreter for more information on the available commands and their usage.

## Usage

To use the Command Interpreter, follow these steps:

1. Run the application using the command `./console.py`.
2. Once the Command Interpreter is running, you will see a prompt `(hbnb)`.
3. Enter commands and arguments to perform operations. For example, to create a new User instance, use the command `create User`.
4. View the output and follow the instructions provided by the Command Interpreter.
5. Repeat the process to perform other operations or use the available commands.

### Non-Interactive Mode

The console can also be used in non-interactive mode:

```
$ echo "create User" | ./console.py

$ echo "help" | ./console.py
```

## Available classes

| Class name | Attributes                                                                                                                                    |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| BaseModel  | `id`, `created_at`, `updated_at`                                                                                                              |
| User       | `email`, `password`, `first_name`, `last_name`                                                                                                |
| State      | `name` `state_id`                                                                                                                             |
| City       | `name`                                                                                                                                        |
| Amenity    | `name`                                                                                                                                        |
| Place      | `city_id` `user_id` `name` `description` `number_rooms` `number_bathrooms` `max_guest` `price_by_night` ` latitude``longitude ` `amenity_ids` |
| Review     | `place_id` `user_id` `text`                                                                                                                   |

## Testing

If you want to personalize the classes and execute unit tests to confirm that your changes haven't modify the functionality use:

```
python3 -m unittest discover tests
```

Alternatively, you can specify a single test file to run at a time:

```
$ python3 unittest -m tests/test_console.py
```

### Questions, Comments, Sugestions

If you have questions or suggestions, contact [AUTHORS](https://github.com/IsmaelMolina-code/holbertonschool-AirBnB_clone/blob/main/AUTHORS)
