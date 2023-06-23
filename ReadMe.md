To identify duplicate images, one method is to calculate a hash value for each image and compare them to one another. If two files have the same hash value, they are duplicates.

Given the path to a hypothetical folder on a hard drive which contains a very large dataset of images, calculate the sha256 has for each, and create a dictionary with a key of the hash string and a value which is a list of file paths for images with that hash.

Keep in mind that processing imagers is a CPU intensive activity and develop a solution that minimizes runtime.
