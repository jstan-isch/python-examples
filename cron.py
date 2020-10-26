# import the required modules
import shutil
import os
import time

# main function
def main():

	# initialize the count
	deleted_folders_count = 0
	deleted_files_count = 0

	# specify the path
	path = "/PATH_TO_DELETE"

	# specify the days
	no_of_days = 90

	# convert days to seconds
	# time.time() returns current time in seconds
	seconds = time.time() - (days * 24 * 60 * 60)

	# check whether the file is present in path or not
	if os.path.exists(path):

		# iterate over each and every folder and file in the path
		for root_folder, folders, files in os.walk(path):

			# compare the days
			if seconds >= get_file_or_folder_age(root_folder):

				# remove the folder
				remove_folder(root_folder)
				deleted_folders_count += 1 # increment count

				# break after remov the root_folder
				break

			else:

				# check folder from the root_folder
				for folder in folders:

					# folder path
					folder_path = os.path.join(root_folder, folder)

					# compare with the days
					if seconds >= get_file_or_folder_age(folder_path):

						# invoke the remove_folder function
						remove_folder(folder_path)
						deleted_folders_count += 1 # increment count


				# check the current directory files
				for file in files:

					# file path
					file_path = os.path.join(root_folder, file)

					# compare the days
					if seconds >= get_file_or_folder_age(file_path):

						# invoke the remove_file function
						remove_file(file_path)
						deleted_files_count += 1 # increment count

		else:

			# if the path is not a directory
			# compare with the days
			if seconds >= get_file_or_folder_age(path):

				# invoke the file
				remove_file(path)
				deleted_files_count += 1 # increment count

	else:

		# file/folder is not found
		print(f'"{path}" is not found')
		deleted_files_count += 1 # increment count

	print(f"Total folders deleted: {deleted_folders_count}")
	print(f"Total files deleted: {deleted_files_count}")


def remove_folder(path):

	# remove the folder
	if not shutil.rmtree(path):

		# success message
		print(f"{path} is removed successfully")

	else:

		# failure message
		print(f"Unable to delete the {path}")



def remove_file(path):

	# remove the file
	if not os.remove(path):

		# success message
		print(f"{path} is removed successfully")

	else:

		# failure message
		print(f"Unable to delete the {path}")


def get_file_or_folder_age(path):

	# get ctime of the file/folder
	# time will be in seconds
	ctime = os.stat(path).st_ctime

	# return the time
	return ctime


if __name__ == '__main__':
	main()