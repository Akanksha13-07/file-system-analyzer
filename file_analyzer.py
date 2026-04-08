import os
import sys

def DirectoryWatcher(path, search_name=None, extension=None):
    # Convert to absolute path if needed
    if not os.path.isabs(path):
        path = os.path.abspath(path)

    # Check if directory exists
    if not os.path.isdir(path):
        print("Invalid path")
        return

    file_count = 0
    folder_count = 0

    with open("output.txt", "w") as f:

        for foldername, subfolders, filenames in os.walk(path):
            f.write(f"\nCurrent Folder: {foldername}\n")
            print(f"\nCurrent Folder: {foldername}")

            for subf in subfolders:
                folder_count += 1
                f.write(f"  Subfolder: {subf}\n")
                print(f"  Subfolder: {subf}")

            for file in filenames:
                full_path = os.path.join(foldername, file)

                # Apply extension filter
                if extension and not file.endswith(extension):
                    continue

                # Apply search filter
                if search_name and search_name.lower() not in file.lower():
                    continue

                file_count += 1
                size = os.path.getsize(full_path)

                f.write(f"  File: {file} | Size: {size} bytes\n")
                print(f"  File: {file} | Size: {size} bytes")

    print("\nSummary:")
    print("Total Files:", file_count)
    print("Total Folders:", folder_count)
    print("Output saved in output.txt")


def main():
    print("Application Name:", sys.argv[0])

    if len(sys.argv) < 2:
        print("Usage: python script.py <path> [search_name] [extension]")
        return

    path = sys.argv[1]

    search_name = None
    extension = None

    if len(sys.argv) >= 3:
        search_name = sys.argv[2]

    if len(sys.argv) == 4:
        extension = sys.argv[3]

    try:
        DirectoryWatcher(path, search_name, extension)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()