# GitHub Unfollowers Detector

GitHub Unfollowers Detector is a Flask web application that allows you to find out who is not following you back on GitHub.

## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Rate Limit](#api-rate-limit)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This web application uses the GitHub API to fetch a user's followers and the accounts they are following. It then compares the two lists to determine the users who are not following the original user back, known as "unfollowers."

## Requirements

- Python 3.x
- Flask (Flask==2.1.1)
- Requests (requests==2.26.0)

## Installation

1. Clone the repository:

```git clone https://github.com/your_username/UnfollowersDetector.git```

```cd UnfollowersDetector```

2. Install the required packages using `pip`:

```pip install -r requirements.txt```


## Usage

1. Run the Flask application:

```python main.py```

2. Access the application in your web browser:
- http://localhost:5000


3. Enter a GitHub username and click the "Detect" button to find the unfollowers.

## API Rate Limit

If you have a premium GitHub account, you can improve the API rate limit by authenticating your requests with a personal access token. Instructions on how to generate a personal access token and use it with the application are provided in the [API rate limit](#api-rate-limit) section of the README.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
