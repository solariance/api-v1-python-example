# Solariance API V1 Client

This repository contains a Python client for interacting with the Solariance API V1. The client is designed to facilitate authentication, retrieve JWT tokens, and fetch forecast power data for a given system ID.

## Features

- **Authentication**: Retrieve JWT tokens for authenticated requests. Each token is valid for 3 days.
- **Forecast Power**: Fetch forecast power data for a specified system ID.

## Prerequisites

- Python 3.10 or higher
- `requests` library

## Installation

Clone the repository: 
```
git clone https://github.com/yourusername/solariance-api-client.git
```

Before using the client, ensure you have set the following environment variables:

- `SOLARIANCE_USER`: Your Solariance username.
- `SOLARIANCE_PWD`: Your Solariance password.
- `SYSTEM_ID`: The ID of the system for which you want to fetch forecast power data.

### Windows

On Windows, you can set environment variables using PowerShell, CMD, or the Graphical User Interface (GUI). There are three different locations to store environment variables:

- **Current Process**: Available to the current shell or application and any child processes started from it. These variables are removed when the process ends.
- **User Registry**: Available to all processes started by the user, accessible only to the user without elevated privileges.
- **Machine Registry**: Available to all users and processes, requires elevated privileges to set.

#### Using PowerShell

To set an environment variable for the current process in PowerShell, use the `$Env` variable:
```
bash export MY_VARIABLE=my_value
```
To make an environment variable persistent across sessions, add the `export` command to your shell's configuration file (e.g., `.bashrc` for Bash or `.zshrc` for Zsh):
```
bash echo 'export MY_VARIABLE=my_value' >> ~/.bashrc # For Bash echo 'export MY_VARIABLE=my_value' >> ~/.zshrc # For Zsh
```

### macOS and Linux

On macOS and Linux, environment variables are typically set in the shell configuration files (e.g., `.bashrc`, `.zshrc`) to ensure they are available in every session.

#### Using Terminal

To set a temporary environment variable for the current session, use the `export` command:
```
bash export MY_VARIABLE=my_value
```
To make an environment variable persistent across sessions, add the `export` command to your shell's configuration file (e.g., `.bashrc` for Bash or `.zshrc` for Zsh):
```
bash echo 'export MY_VARIABLE=my_value' >> ~/.bashrc # For Bash echo 'export MY_VARIABLE=my_value' >> ~/.zshrc # For Zsh
```

After adding the line, reload the configuration file or open a new terminal session to apply the changes.

### Viewing Environment Variables

To view the current environment variables, use the `env` command on macOS and Linux, or the `Get-ChildItem Env:` command in PowerShell on Windows.

### Deleting Environment Variables

To delete an environment variable, use the `unset` command on macOS and Linux, or the `[Environment]::SetEnvironmentVariable('MY_VARIABLE', $null, 'User')` cmdlet in PowerShell on Windows.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss potential improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details
