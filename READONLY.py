
import os.path


#---returns 1 if at least 1 file in directory is read-only---#
def check_readonly(directory=None):
	if directory is None: directory = os.getcwd()
	if os.path.exists(directory):
		for (path, dirs, files) in os.walk(directory):
			for fname in files:
				full_path = os.path.join(path, fname)
				if (os.access(full_path,os.W_OK)==0):
					return 1
				else: return 0	