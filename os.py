# # # os module :
# # """

# # os.path.join(): Combines the directory path with the file name.
# # os.makedirs(): Creates the "Archive" folder if it doesn’t exist.
# # os.stat(file_path).st_mtime: Retrieves the file’s last modified time.
# # datetime.fromtimestamp(): Converts the modification time into a datetime object.
# # (now - mod_time).days: Calculates the file’s age in days.
# # shutil.move(): Moves files older than the threshold to the "Archive" folder.
# # mkdir = make dir ,chdir = change,  getcwd = current working dir,  shutil = copy rw paste garxa or move garna sajilo hunxa ,
# #  rmtree = delete garxa sabaii folder, remove garna aauta file matra remove hunxa4
# # listdir = ley folder bhitra vako list laii dekhaunxa, pwd = present working directory """
# # The uname -a command is used to display detailed information about the operating system and hardware in Unix-like systems (e.g., Linux and macOS). Here's a breakdown:

# # uname: A command that retrieves system information.
# # -a: A flag that requests all available details.
# # import os 
# # import shutil

# # #Create a new directory
# # if not os.path.isdir("Test_directory"):
# #     os.mkdir("test_directory")

# # #Change the current working directory to the new directory
# # os.chdir("test_directory")
# # print("Current working directory: ", os.getcwd())

# # #Create a text file in the directory
# # with open("example.txt", "w") as file:
# #     file.write("This is a text file.")

# # #list files in the current directory
# # print("Files in the directory:", os.listdir())

# # #Copy the file
# # shutil.copy("example.txt", "copy_example.txt")

# # #Move the copied filke to a new location(renaming it in the process)
# # shutil.move("copy_example.txt", "../moved_example.txt")

# # #Go back to the parent directory
# # os.chdir("..")
# # #remove the test directory and its contents
# # shutil.rmtree("test_directory")
# # os.remove("moved_example.txt")#remove the moved file
# # print("cleanup completed!")


# # import subprocess
# # import os

# # #Run a simple command and capture its output

# # result = subprocess.run(["echo", "Hello World!"], capture_output=True, text=True)
# # print("Command Output:", result.stdout)

# # #List files in the current directory using 'ls' or 'dir' (platform-specific)
# # command = ["ls"] if os.name != "nt" else ["dir"]
# # result =subprocess.run(command, capture_output=True, text = True, shell = True)
# # print("Files in current directory:")
# # print(result.stdout)

# # #Check for errors(e.g. invalid command)
# # result = subprocess.run(["Fake_command"], capture_output=True, text = True)
# # if result.returncode != 0:
# #     print("Error:", result.stderr)

# ####################################################################################################################################################3
# import os
# import shutil

# #Define the directory to organiize
# directory = "./example_directory"

# #Create the directory and some text files
# os.makedirs(directory, exist_ok=True)
# with open(os.path.join(directory, "file1.txt"), "w") as f:
#     f.write("Text file content")
# with open(os.path.join(directory, "file2.txt"), "w") as f:
#     f.write("Image file content")
# with open(os.path.join(directory, "file3.txt"), "w") as f:
#     f.write("Audio file content")

# #Function to organize files by type
# def organize_files_by_type(directory):
#     #Get a list of all files in the directory
#     for file_name in os.listdir(directory):
#         file_path = os.path.join(directory, file_name)
#         #Skip directories
#         if os.path.isdir(file_path):
#             continue
#         #Get the file extension
#         file_extension = file_name.split(".")[-1]
#         #Create a folder for the file type f it doesnot exist
#         type_folder = os.path.join(directory, file_extension)
#         os.makedirs(type_folder, exist_ok=True)
#         #Move the file to the appropriate folder
#         shutil.move(file_path, os.path.join(type_folder, file_name))
#         print(f"Moved {file_name} to {type_folder}/")

# #Call the functioin
# organize_files_by_type(directory)

# #Display organized structure

# for root, dirs, files in os.walk(directory):
#     print(f"\nIn {root}:")
#     for dir_name in dirs:
#         print(f"Directory: {dir_name}")
#     for file_name in files:
#         print(f"Directory: {file_name}")

# #Clean up
# #shutil.rmtree(directory)


# """
# Task: Create a script that takes a directory path as input and creates a zip file backup of its contents. 
# The backup file should be named with the current date and time.
# Learning Goals:
# Use os to navigate and identify the directory structure.
# Use shutil for creating archives (shutil.make_archive()).
# Integrate Python’s datetime module for timestamped backups.
# """


# import os
# import shutil
# from datetime import datetime


# if not os.path.isdir("my_folder"):
#     os.mkdir("my_folder")

# zip_file = shutil.make_archive("my_archive", "zip", "my_folder")
# tar_file = shutil.make_archive("my_archive", "tar", "my_folder")
# gztar_file = shutil.make_archive("my_archive", "gztar", root_dir="my_folder")


# current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


# old_file_name = zip_file 
# new_file_name = f"{current_time}.zip"

# try:
#     os.rename(old_file_name, new_file_name)
#     print(f"Archive renamed to: {new_file_name}")
# except FileNotFoundError:
#     print(f"The file '{old_file_name}' does not exist.")
# except Exception as e:
#     print(f"An error occurred: {e}")
# """Next process"""


# import datetime
# import os
# import shutil

# def create_backup(source_directory):
#     if not os.path.exists(source_directory):
#         print(f"Error: The directory '{source_directory}' does not exist. ")
#         return
#     #Generate a timestamped backup name
#     timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
#     backup_name = f"backup_{timestamp}"

#     #Create a zip archive of the source directory
#     shutil.make_archive(backup_name, 'zip', source_directory)
#     print(f"Backup Created: {backup_name}.zip")

# #Example usage
# create_backup("./example_directory")


# """Process Automation with Subprocess
# Task: Automate a system-level task such as:
# Listing all running processes and saving the output to a file.
# Monitoring system resource usage (e.g., CPU and memory stats) by running appropriate system commands (top, ps, or tasklist).
# Learning Goals:
# Use subprocess.run() to execute system commands.
# Capture command output with capture_output=True.
# Write the captured output to a text file for further analysis.
# """
# import subprocess
# import os 
# def list_running_processes(output_file):
#     try:
#         #Execute the system command to list processes
#         command = ['tasklist'] if os.name == 'nt' else ['ps', 'aux']
#         result = subprocess.run(command, capture_output=True, text= True)

#         #Save the output to a file 
#         with open(output_file, 'w') as file:
#             file.write(result.stdout)
#         print(f"Process list saved to '{output_file}'")

#     except Exception as e:
#         print(f"Error: {e}")

# #Example usage
# list_running_processes("pricess_list.txt")



# """. Fun Challenge: File Cleanup Bot
# Task:

# Build a program that:
# Scans a directory for files older than a specified number of days.
# Moves these files to an "Archive" folder.
# Deletes the "Archive" folder after confirming with the user.
# Learning Goals:

# Using os module: To access file metadata (e.g., file modification time using os.stat()).
# Using datetime: To calculate time differences for determining file age.
# User interaction: Using input() to confirm deletion of the "Archive" folder."""

# # import os
# # import shutil
# # from datetime import datetime, timedelta


# # directory = "path_to_directory"  
# # days_threshold = 30  

# # def move_old_files_to_archive(directory, days_threshold):
# #     archive_folder = os.path.join(directory, "Archive")
# #     os.makedirs(archive_folder, exist_ok=True)  

# #     now = datetime.now()
# #     for filename in os.listdir(directory):
# #         file_path = os.path.join(directory, filename)
        
# #         if not os.path.isfile(file_path) or file_path == archive_folder:
# #             continue

# #         mod_time = datetime.fromtimestamp(os.stat(file_path).st_mtime)
# #         file_age = (now - mod_time).days
        
    
# #         if file_age > days_threshold:
# #             print(f"Moving '{filename}' to Archive. It is {file_age} days old.")
# #             shutil.move(file_path, archive_folder)

# # def delete_archive_folder(directory):

# #     archive_folder = os.path.join(directory, "Archive")
# #     if os.path.exists(archive_folder):
# #         confirm = input(f"Do you want to delete the 'Archive' folder? (yes/no): ").strip().lower()
# #         if confirm == "yes":
# #             shutil.rmtree(archive_folder)
# #             print("The 'Archive' folder has been deleted.")
# #         else:
# #             print("The 'Archive' folder was not deleted.")
# #     else:
# #         print("No 'Archive' folder found to delete.")


# # move_old_files_to_archive(directory, days_threshold)
# # delete_archive_folder(directory)

""".................."""
import os
import datetime
import shutil

def file_cleanup_bot(directory, days_old):
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return

    # Calculate the cutoff time
    now = datetime.datetime.now()
    cutoff_time = now - datetime.timedelta(days=days_old)

    # Create an 'Archive' directory
    archive_dir = os.path.join(directory, "Archive")
    os.makedirs(archive_dir, exist_ok=True)

    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Check file's modification time
        file_mtime = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
        if file_mtime < cutoff_time:
            shutil.move(file_path, os.path.join(archive_dir, file_name))
            print(f"Moved '{file_name}' to Archive.")

    # Ask user for confirmation before deleting the archive folder
    confirm = input("Do you want to delete the 'Archive' folder? (yes/no): ").strip().lower()
    if confirm == 'yes':
        shutil.rmtree(archive_dir)
        print("Archive folder deleted.")

# Example usage
file_cleanup_bot(r"C:\path\to\your\directory", 1)


"""5. Creative Project: System Diagnostics Report
Task:

Write a program that generates a system diagnostics report, which includes:
The current working directory.
Disk usage of the current directory.
System information (e.g., OS version, processor, memory).
Save the report as a text file.
Learning Goals:

Using os module: To gather filesystem information (like the current working directory).
Using subprocess module: To execute system commands (e.g., df for disk usage, uname for OS details).
Formatting and saving: Properly format the system diagnostics report and save it to a file.

"""
import os
import shutil
import subprocess

def generate_system_report(output_file):
    try:
        # Get current working directory
        cwd = os.getcwd()

        # Get disk usage of the current directory
        disk_usage = shutil.disk_usage(cwd)

        # Get system information (Windows)
        system_info = subprocess.run(['systeminfo'], capture_output=True, text=True).stdout

        # Write the report to a file
        with open(output_file, 'w') as file:
            file.write(f"Current Working Directory: {cwd}\n")
            file.write(f"Disk Usage:\n")
            file.write(f"  Total: {disk_usage.total / (1024 ** 3):.2f} GB\n")
            file.write(f"  Used: {disk_usage.used / (1024 ** 3):.2f} GB\n")
            file.write(f"  Free: {disk_usage.free / (1024 ** 3):.2f} GB\n")
            file.write(f"System Information:\n{system_info}\n")

        print(f"System diagnostics report saved to '{output_file}'")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
generate_system_report("system_report.txt")






