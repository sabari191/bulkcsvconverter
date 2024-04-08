import os
import xml.etree.ElementTree as ET
import datetime
import fnmatch
import sys

def convert(directory_path, opdir_name):
    now = datetime.datetime.now()
    # format date and time as YYMMDDHHMMSS
    formatted_date_time = now.strftime("%y%m%d%H%M%S")

    # Return Filepaths
    def get_file_paths(directory_path):
        # Convert the file path to the correct format for the current platform
        file_path = os.path.normpath(directory_path)
        file_paths = []
        for root, _, files in os.walk(directory_path):
            for file in files:
                if not fnmatch.fnmatch(file, "*.xml"):
                    continue
                elif fnmatch.fnmatch(file, "*.xml"):
                    file_paths.append(os.path.join(root, file))
        return file_paths

    # Assigning the directory to variable file_paths
    file_paths = get_file_paths(directory_path)
    # MakeDirectory to save the files
    csv_output_path = os.path.join(directory_path, opdir_name)
    print(csv_output_path)
    if not os.path.exists(csv_output_path):
        os.makedirs(csv_output_path)
    # Iterating through the Filepaths
    for file_path in file_paths:
        root = ET.parse(file_path).getroot()
        filename = os.path.basename(file_path)[:-4] + "_" + formatted_date_time + '.csv'
        outfile = os.path.join(csv_output_path, filename)
        delimiter = "["
        root_xpath = "./"
        headers = []

        def create_column_header():
            headers = []
            for elem in root.iter():
                headers.append(elem.tag)
            return headers

        def create_csv_data(Column_Header_List, output_filename):
            with open(output_filename, 'w') as f:
                temp = list(map(str, Column_Header_List))
                print(temp)
                header = str(delimiter.join(temp))
                f.write(header + "\n")
                row = []
                for elem in root.iter():
                    for item in Column_Header_List:
                        if item == elem.tag:
                            if elem is not None and elem.text is not None:
                                row.append(elem.text)
                            else:
                                row.append("")
                print(row)
                tempdata = list(map(str, row))
                dataset = str(delimiter.join(tempdata))
                dataset = dataset.replace("\n", "")
                f.write(dataset + "\n")

        # Example usage
        filtered_headers = create_column_header()
        create_csv_data(filtered_headers, outfile)

    print("---Hey Hi Welcome---")

oprtn = int(input("Enter your option \n1.Convert \n2.Convert and Combine \n3.Combine \n4.Exit -> "))

if oprtn == 1:
    directory_path = input("Enter the directory containing files to convert : ")
    opdir_name = input("Enter the Output Directory name : ")
    # Calling function
    convert(directory_path, opdir_name)
elif oprtn == 2:
    print("WIP.....")
    # directory_path = input("Enter the directory containing files to convert : ")
    # opdir_name = input("Enter the Output Directory name : ")
    # cmbdir_name = input("Enter the combined files Output Directory name : ")
    # Calling function
    # convert(directory_path, opdir_name, cmbdir_name)
elif oprtn == 2:
    print("WIP.....")
    # directory_path = input("Enter the directory containing files to convert : ")
    # opdir_name = input("Enter the Output Directory name : ")
    # cmbdir_name = input("Enter the combined files Output Directory name : ")
    # Calling function
    # convert(directory_path, opdir_name, cmbdir_name)
elif oprtn == 4:
    print("Bye")
    sys.exit()
