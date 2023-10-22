from func import load_pdf, split_text

def get_pdf(PATH):
  data = load_pdf(PATH)
  texts = split_text(data)
  return texts

