def toID(name):
  namestoID = {
      'meth': 0,
      'cocaine': 1,
      'heroin': 2,
      'marijuana': 3,
      'opium': 4
  }
  # Add more mappings as needed

  # Convert the input string to lowercase for case-insensitive matching
  lower_name = name.lower()

  # Check if the input string is in the mapping, otherwise return a default value (e.g., 0)
  return namestoID.get(lower_name, 0)
