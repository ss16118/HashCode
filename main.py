import fileHandler
import makeSlides2
import formSlideShow
import makeSlides

a = "a_example.txt"
b = "b_lovely_landscapes.txt"
c = "c_memorable_moments.txt"
d = "d_pet_pictures.txt"
e = "e_shiny_selfies.txt"

"""
inputData = [a,b,c,d,e]
for data in inputData:
    formSlideShow.makeSlideShow(makeSlides.makeslide(fileHandler.read(data)))

"""
fileHandler.write(formSlideShow.makeSlideShow(makeSlides.makeslide(fileHandler.read(a))), "A - Example.txt")
fileHandler.write(formSlideShow.makeSlideShow(makeSlides.makeslide(fileHandler.read(b))), "B - Lovely landscapes.txt")
fileHandler.write(formSlideShow.makeSlideShow(makeSlides.makeslide(fileHandler.read(c))), "C - Memorable moments.txt")
fileHandler.write(formSlideShow.makeSlideShow(makeSlides.makeslide(fileHandler.read(d))), "D - Pet pictures.txt")
fileHandler.write(formSlideShow.makeSlideShow(makeSlides.makeslide(fileHandler.read(e))), "E - Shiny selfies.txt")
#"""