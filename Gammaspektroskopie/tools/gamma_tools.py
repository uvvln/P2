import numpy as np
from matplotlib import pyplot as plt
from kafe2 import HistContainer, HistFit, Plot
from scipy import special



########################################################################################################################################
# TABLE OF CONTENTS #
# ####################
#
# - Gaussian model function for photopeaks
# - Model function for compton edges using the complementary error function 'erfc' (Convolution of Gaussian and Heaviside-Step-Function) with a quadratic form correction factor 
# - Fit a photopeak using a Gaussian model function
# - Fit a compton edge using a complementary error function
# - Custom wrapper for fitting a custom function to a histogram using Kafe2, combining all relevant steps
#
# #######################################################################################################################################



##########################################
# Gaussian model function for photopeaks #
# #########################################

def gaussian (x, mu, sigma = 50, baseline = 5, s = 0.9, N = 1000, xmin = 0, xmax = 100):
    return  (s / (np.sqrt(2*np.pi) * sigma)) * np.exp(-(x - mu)**2 / (2 * (sigma**2))) + (1-s) * baseline / (xmax-xmin)



################################################################################################################################################################################
# Model function for compton edges using the complementary error function 'erfc' (Convolution of Gaussian and Heaviside-Step-Function) with a quadratic form correction factor #
# ###############################################################################################################################################################################

def compton_edge (x, mu, sigma = 10, A = 1, B = 0.5, baseline = 5, s = 0.9, N = 1000, xmin = 0, xmax = 100):
    return s * special.erfc((x-mu)/(np.sqrt(2) * sigma)) /(2*(mu-xmin))  * (1 + (A * (x/(mu * B) - 1)**2)) + (1-s)*baseline/(xmax-xmin)



###################################################
# Fit a photopeak using a Gaussian model function #
# ##################################################

def fit_peak (datax, datay, x1 = None, x2 = None, label = None, xlabel = 'Channel', ylabel = 'Count', showResult = True, **initparams):
    # Check if a lower x-limit for the fit is given, otherwise use the minimum of the provided dataset
    if x1 == None:
        x1 = min(datax)
    # Check if an upper x-limit for the fit is given, otherwise use the maximum of the provided dataset
    if x2 == None:
        x2 = max(datax)
    # Remove datapoints outside the specified fit range
    datax_clipped = np.delete(datax, np.where((x1 > datax) | (datax > x2)))
    datay_clipped = np.delete(datay, np.where((x1 > datax) | (datax > x2)))
    # Set axis labels
    axislabels = [xlabel, ylabel]
    # Perform a Gaussian fit on the remaining data, choosing the position of the maximum value in the data as an initial value for the position of the peak
    fit = hist_fit_data(datax_clipped, datay_clipped, model = gaussian, limitedparams = [['mu', {'lower':0}], ['sigma', {'lower':0}], ['s', {'lower':0, 'upper':1}]], fixedparams = [["N", np.sum(datay_clipped)], ["xmin", x1], ["xmax", x2]], mu = datax_clipped[np.argmax(datay_clipped)], label = label, showResult = showResult, axislabels = axislabels, **initparams)
    # Return fit object
    return fit



###########################################################
# Fit a compton edge using a complementary error function #
# ##########################################################

def fit_compton (datax, datay, x1 = None, x2 = None, label = None, xlabel = 'Channel', ylabel = 'Count', showResult = True, **initparams):
    # Check if a lower x-limit for the fit is given, otherwise use the minimum of the provided dataset
    if x1 == None:
        x1 = min(datax)
    # Check if an upper x-limit for the fit is given, otherwise use the maximum of the provided dataset
    if x2 == None:
        x2 = max(datax)
    # Remove datapoints outside the specified fit range
    datax_clipped = np.delete(datax, np.where((x1 > datax) | (datax > x2)))
    datay_clipped = np.delete(datay, np.where((x1 > datax) | (datax > x2)))
    # Determine an initial value for the position of the compton edge by estimating where the slope is maximal
    dif = np.diff(datay_clipped)
    diffs = []
    for i in range(len(datay_clipped-25)):
        diffs.append(np.abs(np.sum(dif[i:i+25])))
    mu0 = datax_clipped[np.argmax(diffs)]
    # Set axis labels
    axislabels = [xlabel, ylabel]
    # Perform the fit on the remaining data using the estimated position as an initial value
    fit = hist_fit_data(datax_clipped, datay_clipped, model = compton_edge, limitedparams = [['mu', {'lower':0}], ['sigma', {'lower':0}], ['A', {'lower':0}], ['B', {'lower':0.3, 'upper':0.9}], ['s', {'lower':0, 'upper':1}]], fixedparams = [["N", np.sum(datay_clipped)], ["xmin", x1], ["xmax", x2]], mu = mu0, B = mu0, label = label, axislabels = axislabels, showResult = showResult, **initparams)
    # Return fit object
    return fit



#########################################################################################################
# Custom wrapper for fitting a custom function to a histogram using Kafe2, combining all relevant steps #
# ########################################################################################################

def hist_fit_data (x, y, model = None, label = 'data', constraints = [], fixedparams = [], limitedparams = [], parameternames = None, modellabel = None, modelname = None, axislabels = [None, None], modelexpression = None, report = False, showResult = False, **initialvalues):
    # Organise data histogram container
    step = x[1]-x[0]
    data = HistContainer(bin_edges = np.arange(x[0]-0.5*step, x[-1]+step, step = step))
    data.set_bins(y)
    data.label = label  
    data.axis_labels = axislabels
    # Assign data and model to fit
    fit = HistFit(data, model_function = model, density = True)  
    # Assign parameter constraints and set as initial values
    for a in constraints:
        fit.add_parameter_constraint(name = a[0], value = a[1], uncertainty = a[2])
        fit.set_parameter_values(**{a[0]:a[1]})  
    # Assign fixed parameter values (Causes errors concerning non-positive uncertainties)
    for b in fixedparams:
        fit.fix_parameter(name = b[0], value = b[1])   
    # Assign additional initial values
    fit.set_parameter_values(**initialvalues)
    # Limit parameters to be either zero or positive, not negative
    for a in limitedparams:
        fit.limit_parameter(a[0], **a[1])
    #Assign parameter names as well as model label, name and expression
    if parameternames != None:
        fit.assign_parameter_latex_names(**parameternames)
    if modellabel != None:
        fit.model_label = modellabel
    if modelname != None:
        fit.assign_model_function_latex_name(modelname)
    if modelexpression != None:
        fit.assign_model_function_latex_expression(modelexpression)
    # Perform fit
    fit.do_fit()  
    # Plot fit results if desired
    if showResult:
        p = Plot(fit)
        p.plot()
        plt.show()
    # Report fit results if desired
    if report:
        fit.report()
    # Return fit
    return fit
