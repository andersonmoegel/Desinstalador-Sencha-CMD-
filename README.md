# Sencha Cmd Uninstallation Script (Current User) – Documentation

This script is responsible for uninstalling **Sencha Cmd** from an installation located at `C:\Users\<username>\bin\Sencha`. It removes related files and folders and logs the removal process to a file.

## Features

1. **Detects Sencha Cmd installation directory for the current user**: Checks if the directory where Sencha Cmd is installed exists under the current user's profile.
2. **Deletes all files and folders**: Removes all contents within the Sencha Cmd installation directory.
3. **Logs the removal**: Writes a success message ("Sencha successfully removed") to a log file upon completion.
4. **Logging path**: The log file is stored at `C:\Windows\Temp\Sencha_Uninstall_Log.txt`.

## Code Structure

### 1. Library Imports

```python
import os
import shutil
import time
import getpass
```

These libraries are used for handling directories and files, and securely fetching the current user's name:
- **`os`**: For file path and directory checks.
- **`shutil`**: For recursively deleting directories.
- **`time`**: To log the date and time of the removal.
- **`getpass`**: To get the current system username safely.

### 2. Configuration Variables

#### Sencha Cmd installation path

```python
base_path = f"C:\\Users\\{getpass.getuser()}\\bin\\Sencha"
```

This is the directory where Sencha Cmd is installed for the current user. The path is dynamically generated using `getpass.getuser()` to make the script user-independent.

#### Log file path

```python
log_path = r"C:\Windows\Temp\Sencha_Uninstall_Log.txt"
```

This is the file where the script logs the removal details, including date and time.

### 3. Functions

#### `log_remocao()`

```python
def log_remocao():
    """Logs 'Sencha successfully removed' message to the log file"""
    try:
        with open(log_path, "a") as log_file:
            log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Sencha successfully removed\n")
        print("Sencha CMD successfully removed!")  # Print to console
    except Exception:
        pass  # Ignore logging errors
```

This function appends a success message to the log file, including the current date and time. Errors during logging are silently ignored.

#### `excluir_arquivos(directory)`

```python
def excluir_arquivos(directory):
    """Deletes all files and folders inside the given directory"""
    removed = False
    for root, dirs, files in os.walk(directory, topdown=False):
        for name in files:
            try:
                os.remove(os.path.join(root, name))
                removed = True
            except Exception:
                pass
        for name in dirs:
            try:
                shutil.rmtree(os.path.join(root, name))
                removed = True
            except Exception:
                pass
    return removed
```

This function recursively walks through the directory and removes all its contents. It returns `True` if any files or folders were removed, or `False` otherwise.

#### `desinstalar_sencha()`

```python
def desinstalar_sencha():
    """Uninstalls Sencha Cmd by deleting its files"""
    if os.path.exists(base_path):
        if excluir_arquivos(base_path):
            log_remocao()
    else:
        print("Directory not found. Sencha Cmd might not be installed.")  # No log created
```

This function checks if the installation directory exists. If it does, it attempts to delete its contents and logs the result. If the directory is missing, it prints a warning and skips logging.

### 4. Script Execution

```python
if __name__ == "__main__":
    desinstalar_sencha()
```

Ensures the script runs only when executed directly (not imported). It triggers the uninstallation process.

## Usage

1. **Run the script**: Execute the script in a Python environment. It will check for the Sencha Cmd installation in the current user's directory and remove it if found.
2. **Check the log**: After execution, review the log at `C:\Windows\Temp\Sencha_Uninstall_Log.txt` to confirm successful uninstallation.

## Potential Improvements

- **Enhanced error logging**: Instead of silently ignoring errors, the script could log detailed exceptions for better troubleshooting.
- **Permission checks**: The script could be expanded to verify user permissions before attempting deletions.

## Conclusion

This script automates the uninstallation of Sencha Cmd for the current user. It ensures a clean removal of files and logs the action for traceability and auditing purposes.
