#import
import pyrec as pyr

#create pyro object
presented=[[['cat', 'bat', 'hat', 'goat'],['zoo', 'animal', 'zebra', 'horse']]]
recalled=[[['bat', 'cat', 'goat', 'hat'],['animal', 'horse', 'zoo']]]
pyro = pyr.Pyro(pres=presented,rec=recalled)

#analysis
analyzed_data = pyr.lag_crp(pyro)

#plot
pyr.plot(analyzed_data)
