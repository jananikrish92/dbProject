import numpy as np
import matplotlib.pyplot as plt


def linechart(Labelsi,Value):
	plt.plot(Labelsi, Value)
	plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)
	plt.grid(True) #Turn the grid on
	plt.ylabel("Score") #Y-axis label
	plt.xlabel("table names") #X-axis label
	#plt.title("Train RMSE/Validation RMSE vs max_depth for min_samples_split = 2") #Plot title
	#plt.xlim(0,1000) #set x axis range
	#plt.ylim(-.1,6) #Set yaxis range
	#plt.xticks(range(len(Labelsi)), x_axis, size='small')
	plt.savefig("/Users/jananikrishna/Documents/dbProject/Plot1.jpg")
	#plt.show()



#Labelsi = ['name_1900', 't2', 'name_1910', 't3', 't1']
Value = [0.07352146220938077, 0.7365495524443777, 0.07352146220938077, 1.1749196420074441, 0.21785902950678723]
linechart(range(5),Value)



