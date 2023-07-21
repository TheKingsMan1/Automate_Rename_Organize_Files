#!/usr/bin/python
# -*- encoding: utf-8 -*-

from datetime import datetime
from pathlib import Path

'''
information about path and files 
"E:\Programming_Languages\Excel_Files"
file.parent to get dir or parent of the file
file.stem to get the file_name
file.suffix to get extension of the file 
'''
# path_files = Path('C:\\Users\\Public\\Excel_Files')
path_files = Path("E:/Programming_Languages/Excel_Files")

for file in path_files.iterdir():
    if file.name != '.DS_Store' and file.is_file():
        directory = file.parent
        # file_name = file.stem
        extension = file.suffix

        old_name = file.stem
        region, report_type, old_date = old_name.split('-')

        old_date = datetime.strptime(old_date,'%Y%b%d')
        date = datetime.strftime(old_date, '%Y-%m-%d')

        new_name = f'{region}-{report_type} - {date}{extension}'

        month = datetime.strftime(old_date, '%B') #separete each month

        new_path = path_files.joinpath(month)  #for each mont, create a path
        # file.rename(Path(directory, new_name))
        if not new_path.exists():
            new_path.mkdir()

        new_file_path = new_path.joinpath(new_name)

        file.rename(new_file_path)
