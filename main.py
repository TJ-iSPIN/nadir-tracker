from circleCenterInView import circleCenterInView
from blurFile import blurImg


blurVar=blurImg("earth.jpeg")
blurVar.blur()
blurredImg = circleCenterInView("blurred.jpeg")
blurredImg.inView()
