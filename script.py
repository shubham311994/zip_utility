import tarfile
import zipfile
import gzip
import shutil
import argparse
import sys
import os
from pathlib import Path


def check_file_exists(file_path: str) -> bool:
    """Check if the file exists in a particular path.
    :param: file_path: file path in string format.
    :return: boolean
    """
    file_path = Path(file_path)
    check_file_exist = file_path.is_file()

    return check_file_exist


def check_file_type(file_path: str) -> str:
    """Check the format of the file.
    :param: file_path: file path in str format with the file type.
    :return: file_type: file type in the str format.
    """
    if file_path.endswith('zip'):
        return 'zip'
    elif file_path.endswith('gz'):
        return 'gz'
    elif file_path.endswith('tar'):
        return 'tar'
    else:
        return 'Unsupported Format'


def extract_zip(file_path: str) -> bool:
    """
    Extract the zip format file on the given path.
    :param: file_path: file path in string format
    """
    # TODO: Add code for linux/unix direct os commands
    try:
        if zipfile.is_zipfile(Path(file_path)):
            with zipfile.ZipFile(Path(file_path),'r') as zip_file:
                zip_file.extractall()
                print(f"Zip Files are extracted in {os.getcwd()}")
            return True
        else:
            raise zipfile.BadZipfile("Its not a zip file")
            return False
    except zipfile.BadZipfile:
        return False

def extract_tar(file_path: str) -> bool:
    """
    Extract the tar format file on the given path.
    :param: file_path: file path in string format
    """
    # TODO: Add code for linux/unix direct os commands
    try:
        if tarfile.is_tarfile(file_path):
            with tarfile.open(Path(file_path),tar_flag) as zip_file:
                zip_file.extractall()
                print(f"Files are extracted in {os.getcwd()}")
                return True
        else:
            raise tarfile.TarError("Its not a tarfile.")
            return False
    except tarfile.ExtractError:
        return False

def extract_gz(file_path: str) -> bool:
    """
    Extract the tar format file on the given path.
    :param: file_path: file path in string format
    """
    # TODO: Add code for linux/unix direct os commands
    file_out_path = file_path[:-3]
    try:
        with gzip.open(file_path, 'r') as f_in, open(file_out_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
            return True
    except gzip.BadZipFile:
        return False

def check_os_type() -> str:
    """Check the type of the operating system.
    :return: os_type: type of the operating system in str format.
    """
    return sys.platform


def main(file_path):
    """
    Run the different checks and then extract the file according to particular format.
    :param: file_path: path of the file in string format.
    """
    file_exits = check_file_exists(file_path)
    if file_exits:
        #os_type = check_os_type()
        file_type = check_file_type(file_path)
        if file_type != "Unsupported Format":
            if file_type == "zip":
                extract_zip(file_path)
            if file_type == 'tar':
                extract_tar(file_path)
            if file_type == "gz":
                extract_gz(file_path)
        else:
            raise TypeError(f'The file type is unsupported for extraction {file_path}')
    else:
        raise FileNotFoundError(f"File does not exist at {file_path}")

            
if __name__ == '__main__':
    # TODO: Add extraction path to the code.
    parser = argparse.ArgumentParser()
    parser.add_argument("--path",
                        type=str,
                        help="Please specify the full path of the file to be extracted.",
                        required=True)
    args = parser.parse_args()
    main(args.path)
