from django.db import models

# Create your models here.
class Cola1(models.Model):

    label = models.CharField(max_length=100, blank=False)
    diagonals = models.CharField(max_length=100, blank=False)
    sides = models.CharField(max_length=100, blank=False)
    positions = models.CharField(max_length=100, blank=False)
    positions_y = models.CharField(max_length=100, blank=False)
    name = models.CharField(max_length=100, blank=False)



    def __str__(self):
        return 'label: {0} diagonal:{1} side:{2} positionx:{3} positiony:{4} name:{5}'.format(self.label, self.diagonals, self.sides, self.positions, self.positions_y, self.name)

class ColaFridge(models.Model):

    label = models.CharField(max_length=100, blank=False)
    diagonals = models.CharField(max_length=100, blank=False)
    sides = models.CharField(max_length=100, blank=False)
    positions = models.CharField(max_length=100, blank=False)
    positions_y = models.CharField(max_length=100, blank=False)
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return 'label: {0} diagonal:{1} side:{2} positionx:{3} positiony:{4} name:{5}'.format(self.label, self.diagonals, self.sides, self.positions, self.positions_y, self.name)

class ColaRedShelf(models.Model):

    label = models.CharField(max_length=100, blank=False)
    diagonals = models.CharField(max_length=100, blank=False)
    sides = models.CharField(max_length=100, blank=False)
    positions = models.CharField(max_length=100, blank=False)
    positions_y = models.CharField(max_length=100, blank=False)
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return 'label: {0} diagonal:{1} side:{2} positionx:{3} positiony:{4} name:{5}'.format(self.label, self.diagonals, self.sides, self.positions, self.positions_y, self.name)


class Panorama(models.Model):

    label = models.CharField(max_length=100, blank=False)
    diagonals = models.CharField(max_length=100, blank=False)
    sides = models.CharField(max_length=100, blank=False)
    positions = models.CharField(max_length=100, blank=False)
    positions_y = models.CharField(max_length=100, blank=False)
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return 'label: {0} diagonal:{1} side:{2} positionx:{3} positiony:{4} name:{5}'.format(self.label, self.diagonals, self.sides, self.positions, self.positions_y, self.name)


class ColaFridgeImage(models.Model):
    red = models.CharField(max_length=100, blank=False)
    green = models.CharField(max_length=100, blank=False)
    blue = models.CharField(max_length=100, blank=False)
    overall = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return 'red:{0} green:{1} blue:{2} overall{3}'.format(self.red, self.green, self.blue, self.overall)


class GlassFridge(models.Model):

    label = models.CharField(max_length=100, blank=False)
    diagonals = models.CharField(max_length=100, blank=False)
    sides = models.CharField(max_length=100, blank=False)
    positions = models.CharField(max_length=100, blank=False)
    positions_y = models.CharField(max_length=100, blank=False)
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return 'label: {0} diagonal:{1} side:{2} positionx:{3} positiony:{4} name:{5}'.format(self.label, self.diagonals, self.sides, self.positions, self.positions_y, self.name)



class PhilipMorris(models.Model):

    label = models.CharField(max_length=100, blank=False)
    diagonals = models.CharField(max_length=100, blank=False)
    sides = models.CharField(max_length=100, blank=False)
    positions = models.CharField(max_length=100, blank=False)
    positions_y = models.CharField(max_length=100, blank=False)
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return 'label: {0} diagonal:{1} side:{2} positionx:{3} positiony:{4} name:{5}'.format(self.label, self.diagonals, self.sides, self.positions, self.positions_y, self.name)

class GlassFridgeImages(models.Model):
    red_mean = models.CharField(max_length=100, blank=False)
    green_mean = models.CharField(max_length=100, blank=False)
    blue_mean = models.CharField(max_length=100, blank=False)
    overall_mean = models.CharField(max_length=100, blank=False)
    red_stand = models.CharField(max_length=100, blank=False)
    green_stand = models.CharField(max_length=100, blank=False)
    blue_stand = models.CharField(max_length=100, blank=False)
    overall_stand = models.CharField(max_length=100, blank=False)

    def __str__(self):
            return 'red_mean: {0} green_mean:{1} blue_mean:{2} overall_mean:{3} red_stand:{4} green_stand:{5} blue_stand:{6} overall_stand:{7}'.format(self.red_mean, self.green_mean, self.blue_mean, self.overall_mean, self.red_stand, self.green_stand, self.blue_stand, self.overall_stand)
