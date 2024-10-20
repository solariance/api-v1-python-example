# Solariance API V1 Client

This repository contains a Python client for interacting with the Solariance API V1. The client is designed to facilitate authentication, retrieve JWT tokens, and fetch forecast power data for a given system ID.

## API Endpoint Documentation
https://developer.solariance.de

## Features

- **Authentication**: Retrieve JWT tokens for authenticated requests. Each token is valid for 14 days.
- **Forecast Power**: Fetch forecast power data for a specified system ID.

## Prerequisites

- Python 3.10 or higher
- `requests` library

## Installation

### Clone the repository: 
```
git clone https://github.com/yourusername/solariance-api-client.git
```

### Setting environment variables

Utilizing environment variables is a preferred method for securing sensitive data, such as credentials, by keeping them separate from the source code.
Ensure you have set the following (environment) variables:

- `SOLARIANCE_USER`: Your Solariance username.
- `SOLARIANCE_PWD`: Your Solariance password.
- `SYSTEM_ID`: The ID of the system for which you want to fetch forecast power data.

#### Windows

On Windows, you can set environment variables using PowerShell, CMD, or the Graphical User Interface (GUI). There are three different locations to store environment variables:

##### Using PowerShell

To set an environment variable for the current process in PowerShell, use the `$Env` variable:
```
bash export MY_VARIABLE=my_value
```
To make an environment variable persistent across sessions, add the `export` command to your shell's configuration file (e.g., `.bashrc` for Bash or `.zshrc` for Zsh):
```
bash echo 'export MY_VARIABLE=my_value' >> ~/.bashrc # For Bash echo 'export MY_VARIABLE=my_value' >> ~/.zshrc # For Zsh
```

#### macOS and Linux

On macOS and Linux, environment variables are typically set in the shell configuration files (e.g., `.bashrc`, `.zshrc`) to ensure they are available in every session.

##### Using Terminal

To set a temporary environment variable for the current session, use the `export` command:
```
bash export MY_VARIABLE=my_value
```
To make an environment variable persistent across sessions, add the `export` command to your shell's configuration file (e.g., `.bashrc` for Bash or `.zshrc` for Zsh):
```
bash echo 'export MY_VARIABLE=my_value' >> ~/.bashrc # For Bash echo 'export MY_VARIABLE=my_value' >> ~/.zshrc # For Zsh
```

After adding the line, reload the configuration file or open a new terminal session to apply the changes.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss potential improvements or bug fixes.

## Support

If you have any questions or need further assistance, please contact our support team at support@solariance.de.

## License

By using the Solariance API V1, you agree to the following terms:

- **Attribution**: You must provide attribution to **Solariance** in any derivative works, publications, or products that use the Solariance API. The attribution must clearly state: "Powered by Solariance" or "Data provided by Solariance API."
- **Non-Commercial Use**: The Solariance API V1 is free to use for non-commercial purposes only. Any commercial use of the Solariance API V1 (including, but not limited to, use in a product or service that is sold or monetized) requires explicit permission from Solariance.
- **Permission for Commercial Use**: To request permission for commercial use, please contact [sales@solariance.de](mailto:sales@solariance.de) with details about your intended use.

This license ensures that any use of the Solariance API V1 is properly credited and restricts commercial use without prior approval. If you have any questions about licensing, please contact [support@solariance.de](mailto:support@solariance.de).
