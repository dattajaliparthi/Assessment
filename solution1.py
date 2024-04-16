  import sys
  import os

  if len(sys.argv) != 2:
      print("Usage: python create_shared_directory.py <path_to_directory>")
      sys.exit(1)

  dir_path = sys.argv[1]

  try:
      os.makedirs(dir_path, exist_ok=True)
      os.chmod(dir_path, 0o777)
      print(f"Shared directory '{dir_path}' created successfully.")
  except Exception as e:
      print(f"Failed to create shared directory: {e}")

  Assumptions made:

  Developers have SSH/SFTP access to the server.
  The script is run with sufficient privileges to create directories and set permissions

