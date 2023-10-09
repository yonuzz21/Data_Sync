import os ,shutil ,schedule ,logging
import time as tm



def sync_folders(source_dir, destination_dir):
    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_dir):
        shutil.copy(source_dir, destination_dir)


    # Sync the folders
    for root, dirs, files in os.walk(destination_dir, topdown=True):
        # Remove any files in the destination that no longer exist in the source
        for file in files:
            destination_file = os.path.join(root, file)
            if os.path.exists(destination_file):
                os.remove(destination_file)
                print(f"Deleted: {destination_file}")
                logging.info(f"[Deleted] File: {destination_file} .")


        # Remove any empty directories in the destination
        for dir in dirs:
            destination_dir = os.path.join(root, dir)
            if not os.listdir(destination_dir):
                os.rmdir(destination_dir)
                print(f"Deleted directory: {destination_dir}")
                logging.info(f"[Deleted] Directory: {destination_dir}")
        
        
    # Copy files from source to destination
    shutil.copytree(source_dir, destination_dir, dirs_exist_ok=True)
    print("Synced folders")
    logging.info("[*] Folders synced successfully!")


logging.basicConfig(filename="log.txt",
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)s %(levelname)-8s %(message)s')


test = input("Source: ")    
production = input("Target: ")   

# Run the initial sync
sync_folders(test, production)

# Schedule periodic sync every 3 seconds
schedule.every(3).seconds.do(lambda: sync_folders(test, production))

while True:
    schedule.run_pending()
    tm.sleep(1)
