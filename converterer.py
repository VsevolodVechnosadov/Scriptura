import img2pdf, os
def convert_pdf(dirname: str):
	imgs = []
	for file_name in os.listdir(dirname):
		if not file_name.endswith(".jpg"):
			continue
		path = os.path.join(dirname, file_name)
		if os.path.isdir(path):
			continue
		imgs.append(path)
	pdf_tokens = dirname.split('\\')
	pdf_name = pdf_tokens[-1]
	path_to_pdf = dirname + '\\' + pdf_name + '.pdf'
	with open(path_to_pdf,'wb') as pdf_file:
		pdf_file.write(img2pdf.convert(imgs))
	return path_to_pdf