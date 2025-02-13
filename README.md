# Remove Duplicates Script

## Description

This script removes duplicate lines from a specified text file.

## Usage

1. Ensure you have Python installed on your system.
2. Modify the `file_path` variable in the script to point to the file you want to process.
3. Run (where is located) the script using:

   ```sh
   python DuplicateScript.py

## Notes

- The script reads the file, removes duplicate lines, and writes back the unique lines.
- It modifies the file in place.
- Backup your file before running the script if necessary.

## Example

If your `users.txt` file contains:

```txt
Alice
Bob
Alice
Charlie
```

After running the script, it will be:

```txt
Alice
Bob
Charlie
