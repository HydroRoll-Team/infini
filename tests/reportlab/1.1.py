from reportlab.lib import colors
from reportlab.graphics.shapes import (Drawing, Rect, String, Line, Group)
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.pdfbase.ttfonts import TTFont

# font
registerFont(TTFont("Times", "C:\Windows\Fonts\Times.ttf"))

drawing = Drawing(400, 200)
# beige rectangle
r1 = Rect(0, 0, 400, 200, 0, 0)
r1.fillColor = colors.beige
drawing.add(r1)

# logo
wave = Group(
    Line(10, -5, 10, 10),
    Line(20, -15, 20, 20),
    Line(30, -5, 30, 10),
    Line(40, -15, 40, 20),
    Line(50, -5, 50, 10),
    Line(60, -15, 60, 20),
    Line(70, -5, 70, 10),
    Line(80, -15, 80, 20),
    Line(90, -5, 90, 10),
    String(25, -25, "Wave Audio", fontName='Times')
)
wave.translate(10, 170)
drawing.add(wave)

# save
drawing.save(formats=['pdf', 'png'], outDir=".", fnRoot="card")