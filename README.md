# Overview
This guide explains how to set up and run the **Automated Server Backup Script** using Python. The script will back up specified directories to a designated backup location at scheduled intervals, ensuring your data is protected.

## Requirements
- macOS operating system.
- Python 3 installed on your machine.
- Basic familiarity with the terminal (command line).

## Step 1: Create Project Directory
1. Open the terminal.
2. Navigate to your desired location:
   ```bash
   cd /Users/yourusername
   ```
3. Create a new project directory:
   ```bash
   mkdir AutomateServerBackupScript
   cd AutomateServerBackupScript
   ```

## Step 2: Configuration File
1. Create a file named `backup_config.ini` in the project directory.
2. Add the following content to define the directories to back up, the backup location, and how many backups to keep:
   ```ini
   [backup_settings]
   directories = /path/to/your/directory1, /path/to/your/directory2
   backup_location = /path/to/backup/directory
   max_backups = 5
   ```
3. Replace the placeholder paths with actual directory locations on your system.

## Step 3: Python Script
1. In the same project directory, create a file named `main.py`.
2. Add the script that performs the backup and manages old backups. See `main.py` for the full code.

## Step 4: Make Script Executable
1. In the terminal, navigate to your project directory:
   ```bash
   cd /Users/yourusername/AutomateServerBackupScript
   ```
2. Make the script executable:
   ```bash
   chmod +x main.py
   ```

## Step 5: Schedule the Backup
1. Open your crontab file to schedule the script:
   ```bash
   crontab -e
   ```
2. Add the following line to schedule the script to run at 2 AM every day:
   ```bash
   0 2 * * * /usr/bin/python3 /Users/yourusername/AutomateServerBackupScript/main.py
   ```
3. Save the crontab file.

## Step 6: Verify Setup
- To list your scheduled cron jobs, run:
   ```bash
   crontab -l
   ```
- Check the backup location after the scheduled time to confirm backups are being created.
- Logs of the backup process will be written to `backup_log.txt` in the project directory.

## Important Note: macOS Compatibility
This setup and script are designed for **macOS**. For other operating systems:
- Update file paths accordingly.
- Use Task Scheduler on Windows instead of cron.
- Skip the `chmod +x` step on Windows.

## Additional Resources
- Python Documentation: https://docs.python.org/3/
- Cron Job Guide: https://help.ubuntu.com/community/CronHowto
