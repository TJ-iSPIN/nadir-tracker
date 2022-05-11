from circleCenterInView import circleCenterInView
from blurFile import blurImg

blurVar=blurImg("earth2.jpeg")
blurVar.blur()
blurredImg = circleCenterInView("blurred.jpeg")
x=0
y=0
for i in range(0,100):
    x+=blurredImg.approximater()[0]
    y+=blurredImg.approximater()[1]
print("inview:",blurredImg.inView())
x,y = (int(x/100),int(y/100))
print(x,y)
