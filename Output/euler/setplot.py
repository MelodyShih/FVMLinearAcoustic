
""" 
Set up the plot figures, axes, and items to be done for each frame.

This module is imported by the plotting routines and then the
function setplot is called to set the plot parameters.
    
""" 
# #--------------------------
# def setplot(plotdata):
# #--------------------------
#     """ 
#     Specify what is to be plotted at each frame.
#     Input:  plotdata, an instance of visclaw.data.ClawPlotData.
#     Output: a modified version of plotdata.
#     """ 
#     plotdata.clearfigures()  # clear any old figures,axes,items data

#     plotfigure = plotdata.new_plotfigure(name='', figno=0)

#     plotaxes = plotfigure.new_plotaxes()
#     plotaxes.axescmd = 'subplot(211)'
#     plotaxes.title = 'Density'

#     plotitem = plotaxes.new_plotitem(plot_type='1d')
#     plotitem.plot_var = 0
#     plotitem.kwargs = {'linewidth':3}
    
#     plotaxes = plotfigure.new_plotaxes()
#     plotaxes.axescmd = 'subplot(212)'
#     plotaxes.title = 'Energy'

#     plotitem = plotaxes.new_plotitem(plot_type='1d')
#     plotitem.plot_var = 2
#     plotitem.kwargs = {'linewidth':3}
    
#     return plotdata

#--------------------------
def setplot(plotdata):
#--------------------------
    
    """ 
    Specify what is to be plotted at each frame.
    Input:  plotdata, an instance of clawpack.visclaw.data.ClawPlotData.
    Output: a modified version of plotdata.
    
    """ 


    plotdata.clearfigures()  # clear any old figures,axes,items data

    # Figure for q[0]
    plotfigure = plotdata.new_plotfigure(name='Density', figno=0)

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    plotaxes.axescmd = 'subplot(111)'   # top figure
    plotaxes.xlimits = 'auto'
    plotaxes.ylimits = 'auto'
    plotaxes.title = 'Density'

    # Set up for item on these axes:
    plotitem = plotaxes.new_plotitem(plot_type='1d_plot')
    plotitem.plot_var = 0
    plotitem.plotstyle = '-'
    plotitem.color = 'b'


    # Figure for q[1]
    plotfigure = plotdata.new_plotfigure(name='Energy', figno=1)
    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    plotaxes.axescmd = 'subplot(111)'   # bottom figure
    plotaxes.xlimits = 'auto'
    plotaxes.ylimits = 'auto'
    plotaxes.title = 'Energy'

    # Set up for item on these axes:
    plotitem = plotaxes.new_plotitem(plot_type='1d_plot')
    plotitem.plot_var = 2
    plotitem.plotstyle = '-'
    plotitem.color = 'b'

    # Parameters used only when creating html and/or latex hardcopy
    # e.g., via clawpack.visclaw.frametools.printframes:

    plotdata.printfigs = True                # print figures
    plotdata.print_format = 'png'            # file format
    plotdata.print_framenos = 'all'          # list of frames to print
    plotdata.print_fignos = 'all'            # list of figures to print
    plotdata.html = True                     # create html files of plots?
    plotdata.html_homelink = '../README.html'
    plotdata.latex = True                    # create latex file of plots?
    plotdata.latex_figsperline = 2           # layout of plots
    plotdata.latex_framesperline = 1         # layout of plots
    plotdata.latex_makepdf = False           # also run pdflatex?

    return plotdata

    
