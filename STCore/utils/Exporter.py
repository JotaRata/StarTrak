
import tkFileDialog
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib import figure
def ExportImage(figure):
	path = tkFileDialog.asksaveasfilename(confirmoverwrite = True, filetypes=[("Portable Network Graphics", "*.png"), ("JPEG Image", "*.jpg")], defaultextension = "*.png")
	figure.savefig(str(path))

def ExportData(TrackedStars, MagData, TimeLabel):
	path = tkFileDialog.asksaveasfilename(confirmoverwrite = True, filetypes=[("Archivo de texto", "*.txt")], defaultextension = "*.txt")
	with open(path, "wb") as f:
		print >>f, "Magnitudes aparentes de "+str(len(TrackedStars))+" estrellas"
		print >>f, "Generado por StarTrak"
		print >>f, " "
		names = "Fechas\t"
		for t in TrackedStars:
			names += t.star.name+ "\t"
		print >>f, names
		i = 0
		while i < MagData.shape[1]:
			line = TimeLabel[i]+"\t"
			j = 0
			while j < MagData.shape[0]:
				line += ('%.2f' % MagData[j][i])+"\t"
				j += 1
			print >>f, line
			i += 1

def ExportPDF(fig, MagData, TrackedStars):
		path = tkFileDialog.asksaveasfilename(confirmoverwrite = True, filetypes=[("Documento PDF", "*.pdf")], defaultextension = "*.pdf")
		collabel = []
		fig.set_size_inches(7, 4)
		for t in TrackedStars:
			collabel.append(t.star.name)
		tableFig = figure.Figure(figsize = (7, 4), dpi= 100)
		tableAx = tableFig.add_subplot(111)
		tableAx.set_axis_off()
		tableAx.table(cellText=MagData.transpose().round(decimals = 2),colLabels=collabel,loc='center')
		with PdfPages(str(path)) as pp:
			
			pp.savefig(fig)
			pp.savefig(tableFig)