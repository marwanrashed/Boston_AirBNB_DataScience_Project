# Import nessecary packages and libararies
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

class VizTool ():
    def __init__ (self):
        # Set the style globally
        # Alternatives include bmh, fivethirtyeight, ggplot,
        # dark_background, seaborn-deep, etc
        plt.style.use('seaborn-deep')

        plt.rcParams['font.family'] = 'serif'
        plt.rcParams['font.serif'] = 'Ubuntu'
        plt.rcParams['font.monospace'] = 'Ubuntu Mono'
        plt.rcParams['font.size'] = 16
        plt.rcParams['axes.labelsize'] = 16
        plt.rcParams['axes.labelweight'] = 'bold'
        plt.rcParams['axes.titlesize'] = 16
        plt.rcParams['xtick.labelsize'] = 14
        plt.rcParams['ytick.labelsize'] = 14
        plt.rcParams['legend.fontsize'] = 16
        plt.rcParams['figure.titlesize'] = 18

    def line_plot (self,parameter, title, xlabel, ylabel, legend,fig_size = [8,5]):
        plt.figure(figsize = fig_size); 
        plt.plot(parameter, label = legend, color= '#3690c0');
        plt.xlabel(xlabel);
        plt.ylabel(ylabel);
        plt.title(title);
        plt.legend();
        plt.show()
    def ShowTwoVariable_lineplot (self,parameter1,parameter2, title, xlabel, ylabel, legend1,legend2,fig_size = [8,5]):
        plt.figure(figsize = fig_size); 
        plt.plot(parameter1, label = legend1);
        plt.plot(parameter2, label = legend2);
        plt.xlabel(xlabel);
        plt.ylabel(ylabel);
        plt.title(title);
        plt.legend();
        plt.show()
    def Plot_Distribution (self,parameter,title, xlabel, ylabel, legend, fig_size = [8,5]):
        plt.figure(figsize = fig_size); 
        sns.distplot(parameter, label = legend);
        plt.xlabel (xlabel);
        plt.ylabel(ylabel);
        plt.title(title);
        plt.legend();
        plt.show()
    def Plot_Hist (self,parameter,axis,title = None, xlabel = None, ylabel = None, legend = None,minimum = 0, maximum = 0, step = 0, fig_size = [8,5],r_width = 0.7,vis_x= True,vis_y = True,vis_legend = True):
        plt.figure(figsize = fig_size); 
        bins = np.arange(minimum, maximum, step)
        plt.hist(parameter, label = legend, bins = bins, color= '#3690c0', rwidth = r_width);
        plt.title(title);
        plt.xlabel (xlabel).set_visible(vis_x);
        plt.ylabel (ylabel).set_visible(vis_y);
        plt.legend().set_visible(vis_legend);
        plt.xlim(axis);
    def Plot_HistLog (self,parameter,axis,title = None, xlabel = None, ylabel = None, legend = None,minimum = 0, maximum = 0, step = 0, fig_size = [8,5],r_width = 0.7,vis_x= True,vis_y = True,vis_legend = True):
        plt.figure(figsize = fig_size); 
        bins = 10 **np.arange(minimum, np.log10(maximum)+step , step)
        plt.hist(parameter, label = legend, bins = bins, rwidth = r_width);
        plt.title(title);
        plt.xlabel (xlabel).set_visible(vis_x);
        plt.ylabel (ylabel).set_visible(vis_y);
        plt.legend().set_visible(vis_legend);
        plt.xscale('log')
        plt.xlim(axis);
    def Plot_Count (self,parameter,title, xlabel, ylabel, legend, fig_size = [8,5]):
        plt.figure(figsize = fig_size);
        color_base = sns.color_palette()[0]
        sns.countplot(x = parameter, color= '#3690c0', label = legend);
        plt.title(title);
        plt.xlabel (xlabel);
        plt.ylabel (ylabel);
        plt.legend();
        plt.show()
    def Plot_bar (self,parameter1, parameter2, xlabel,ylabel,title,Rotation = 90):
        plt.figure(figsize = [15, 5]) 
        sns.barplot(x = parameter1,  y = parameter2, color= '#3690c0')
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title);
        plt.xticks(rotation = Rotation)
        plt.show()
    def Plot_barProp (self,parameter1, parameter2,Total_count, counts, xlabel,ylabel,title,fig_size = [8, 5],Rotation = 90):
        # rcParams['figure.figsize'] = 12,4
        plt.figure(figsize = fig_size) 
        plt.bar(parameter1,parameter2, color= '#3690c0')
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title);
        locs, labels = plt.xticks(rotation=Rotation) 
        # loop through each pair of locations and labels
        for loc, label in zip(locs, labels):
            #count = counts[i]
            # Convert count into a percentage, and then into string
            pct_string = '{:0.1f}%'.format(100*count/Total_count)
            # Print the string value on the bar. 
            # Read more about the arguments of text() function [here](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.text.html)
            plt.text(loc, labels, pct_string, va='center', ha = 'center')

            plt.text(loc, labels, pct_string, va='center', ha = 'center')
    def Plot_barhProp (self,parameter1, parameter2,Total_count, counts, xlabel,ylabel,title,fig_size = [20, 10],Rotation = 90):
        # rcParams['figure.figsize'] = 12,4
        plt.figure(figsize = fig_size) 
        plt.barh(parameter1,parameter2, color= '#3690c0')
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title);
        locs, labels = plt.xticks(rotation=Rotation) 
        # loop through each pair of locations and labels
        for i in range (len(counts)):
            # Remember, type_counts contains the frequency of unique values in the `type` column in decreasing order.
            count = counts[i]
            # Convert count into a percentage, and then into string
            pct_string = '{:0.1f}%'.format(100*count/Total_count)
            # Print the string value on the bar. 
            # Read more about the arguments of text() function [here](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.text.html)
            plt.text(count+1, i, pct_string, va='center')

