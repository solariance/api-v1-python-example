# Solariance API Client

This repository contains a Python client for interacting with the Solariance API. The client is designed to facilitate authentication, retrieve JWT tokens, and fetch forecast power data for a given system ID.

## Features

- **Authentication**: Retrieve JWT tokens for authenticated requests.
- **Forecast Power**: Fetch forecast power data for a specified system ID.

## Prerequisites

- Python 3.10 or higher
- `requests` library

## Installation

1. Clone the repository: git clone https://github.com/yourusername/solariance-api-client.git

## Usage

Before using the client, ensure you have set the following environment variables:

- `SOLARIANCE_USER`: Your Solariance username.
- `SOLARIANCE_PWD`: Your Solariance password.
- `SYSTEM_ID`: The ID of the system for which you want to fetch forecast power data.

To run the client and fetch forecast power data, execute the script:

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss potential improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details