from circleCenterInView import circleCenterInView
from blurFile import blurImg

blurVar=blurImg("earth2.jpeg")
blurVar.blur()
blurredImg = circleCenterInView("blurred.jpeg")
blurredImg.approximater()
