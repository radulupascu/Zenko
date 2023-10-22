from func import load_csv, csv_to_text


def get_csv(PATH):
  data = load_csv(PATH)
  csv_to_text(data)
  text = csv_to_text(data)
  return text

