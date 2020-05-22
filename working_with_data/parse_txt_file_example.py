import csv
import subprocess
import pandas as pd

def parse_viya_status_file(in_file_name='status_file.txt'):
    cmd = 'cp status_file_copy.txt ' + in_file_name
    subprocess.call([cmd], shell=True)
    """
    Parse viya status file and save it in data frame
    """
    with open(in_file_name, 'r') as in_file:
        csv_reader = csv.reader(in_file, delimiter=' ')
        line_count = 0
        for row in csv_reader:
            # remove empty spaces
            filtered_data = [line for line in row if line != '']
            if line_count == 1:
                #create header
                data = pd.DataFrame([], columns=filtered_data)
                line_count += 1
            elif line_count >= 1 and len(filtered_data) > 4: #exclude summary from the status file
                a_series = pd.Series(filtered_data, index=data.columns)
                data = data.append(a_series, ignore_index=True)
                line_count += 1
            else:
                line_count += 1
        return data