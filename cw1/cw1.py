import os
import shutil


def is_image_file(file):
    return file.lower().endswith(("jpg", "png"))


# Creating new directory
new_directory = "copies"
base_directory = "/Users/Kamil/Documents/WSEI studia/pythonLab3/cw1"
copies_directory = os.path.join(base_directory, new_directory)
os.makedirs(copies_directory, exist_ok=True)

# creating report file
report_file = os.path.join(base_directory, "report.txt")

with open("report_file", "w") as report:
    folders = [f for f in os.listdir(base_directory) if os.path.isdir(os.path.join(base_directory, f))]

    for f in folders:
        current_folder = os.path.join(base_directory, f)

        image_files = [file for file in os.listdir(current_folder) if is_image_file(file)]

        # writing in report file
        report.write(f"Folder: {current_folder}\n")
        report.write("Old file names:\n")
        for image_file in image_files:
            report.write(f"- {image_file}\n")

        # copying and adding new file names
        for i, image_file in enumerate(image_files):
            new_filename = f"{f}_{i}.jpg" if image_file.lower().endswith(('.jpg')) else f"{f}_{i}.png"

            source_file = os.path.join(current_folder, image_file)
            destination_file = os.path.join(copies_directory, new_filename)

            shutil.copy(source_file, destination_file)

            report.write(f"  Files copied: {source_file} -> {destination_file}\n")

print("The operation has been completed. The report has been saved in the file:", report_file)



