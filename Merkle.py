import hashlib
import os
import sys


def get_file_hash(filepath):
    """Returns the SHA1 hash of the file at the given filepath"""
    #create Sha1 hash
    sha1_hash = hashlib.sha1()
    #open file in biunary
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
        #update the hash object and return hex hash
            sha1_hash.update(chunk)
    return sha1_hash.hexdigest()


def compute_top_hash(filepaths):
    """Computes the Top Hash of a list of filepaths"""
    #get hash for multiple files
    file_hashes = [get_file_hash(filepath) for filepath in filepaths]
    #new tophash object to save the result in
    top_hash = hashlib.sha1()
    #update the tophash object with sha1 from each file
    for file_hash in file_hashes:
        top_hash.update(file_hash.encode('utf-8'))
    return top_hash.hexdigest()


if __name__ == '__main__':
    #get filepaths from commandline
    filepaths = sys.argv[1:]
    #check if at least one file was added - I didnt get a chance to add checks for existing files, so if a file is added that doesnt exist, the program will crash
    if not filepaths:
        print('Please provide the pathnames')
        sys.exit(1)
    #calculate tophash and print it
    print(f'Computing Top Hash of {len(filepaths)} files...')
    top_hash = compute_top_hash(filepaths)
    print(f'Top Hash: {top_hash}')