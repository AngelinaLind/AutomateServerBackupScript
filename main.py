import os
import configparser
import datetime
import shutil
import logging

# Step 1: Configure logging
logging.basicConfig(
    filename='backup_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Step 2: Read the configuration file
config = configparser.ConfigParser()
config.read('backup_config.ini')

# Step 3: Extract values from the config
backup_location = config['backup_settings']['backup_location']
directories = config['backup_settings']['directories'].split(', ')
max_backups = int(config['backup_settings']['max_backups'])

logging.info("Starting backup process")
logging.info("Directories to back up: %s", directories)
logging.info("Backup location: %s", backup_location)
logging.info("Max backups to keep: %d", max_backups)

# Step 4: Create a backup directory with a timestamp
timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
backup_folder = os.path.join(backup_location, f'backup_{timestamp}')
os.makedirs(backup_folder)
logging.info("Created backup folder: %s", backup_folder)

# Step 5: Copy each directory to the backup folder
for directory in directories:
    try:
        dir_name = os.path.basename(directory.rstrip('/'))
        target_directory = os.path.join(backup_folder, dir_name)
        shutil.copytree(directory, target_directory)
        logging.info("Successfully backed up: %s to %s", directory, target_directory)
    except Exception as e:
        logging.error("Error while backing up %s: %s", directory, e)


# Step 6: Manage the number of backups
def manage_backups(max_backups):
    backups = [d for d in os.listdir(backup_location) if os.path.isdir(os.path.join(backup_location, d))]

    # Sort backups by creation time (oldest first)
    backups.sort(key=lambda x: os.path.getctime(os.path.join(backup_location, x)))

    while len(backups) > max_backups:
        oldest_backup = backups.pop(0)  # Get the oldest backup
        backup_path = os.path.join(backup_location, oldest_backup)
        try:
            shutil.rmtree(backup_path)  # Delete the folder
            logging.info("Deleted old backup: %s", oldest_backup)
        except Exception as e:
            logging.error("Error deleting backup %s: %s", oldest_backup, e)


# Call the manage_backups function
manage_backups(max_backups)
