# Import packages
import cmasher as cmr
#cmr.__version__
#'1.5.0'

# in case you don't have cmasher, install it
#!pip install cmasher

def create_cmasher_tableau_properties_file(cmap_range=(0.15,0.85)):
	"""
    Create Tableau parameters.tps file that contains colormaps from the python package CMasher
    
    Parameters:
    ==========
    colormap_range: input two float numbers in range (0, 1)
    
    Returns:
    =======
    Parameters.tps -- Tableau preferences file with CMasher's colormaps
    """
    # Get colormaps
	cmr.cm.cmap_d.keys()

	# Get type of the colormaps
	cmr.cm.cmap_cd.keys()

	# There are only sequential and diverging colormaps
	# We obtain names of colormaps using only those that do not end with '_r' since they are the reversed version of each colormap
	sequential_colormap = [y for y in cmr.cm.cmap_cd['sequential'] if not y.endswith('_r')]
	diverging_colormap = [y for y in cmr.cm.cmap_cd['diverging'] if not y.endswith('_r')]

	# Get the HEXZ values of each sequential colormaps 
	# Export them in range of: 0.15 to 0.85 -> you can export the full range if you prefer.
	all_sequential_maps_hex = []
	for colormap in sequential_colormap:
		cmp = cmr.take_cmap_colors('cmr.{}'.format(colormap), None, cmap_range=cmap_range, return_fmt='hex')
		all_sequential_maps_hex.append(cmp)

    # Get the hex values of the diverging colormaps; in range 0.15 to 0.85
	all_diverging_maps_hex = []
	for colormap in diverging_colormap:
		cmp = cmr.take_cmap_colors('cmr.{}'.format(colormap), None, cmap_range=cmap_range, return_fmt='hex')
		all_diverging_maps_hex.append(cmp)

	with open("Preferences.tps", 'w') as f:

		print("<?xml version='1.0'?>", file=f)
		print("<workbook>", file=f)
		print("    <preferences>", file=f)

	    # Get all the sequential colormaps in the format that is required in Tableau
		for i, hexes in enumerate(all_sequential_maps_hex):
			print('    <color-palette name='+'"'+'{}'.format(sequential_colormap[i])+'" ' +'type="ordered-sequential">', file=f)
			for j, col in enumerate(hexes):
				print('        <color>'+'{}'.format(hexes[j])+'</color>', file=f)
			print('    </color-palette>', file=f)

	 	# Get all the diverging colormaps in the format that is required in Tableau
		for i, hexes in enumerate(all_diverging_maps_hex):
			print('<color-palette name='+'"'+'{}'.format(diverging_colormap[i])+'" ' +'type="ordered-diverging">', file=f)
			for j, col in enumerate(hexes):
				print('        <color>'+'{}'.format(hexes[j])+'</color>', file=f)
			print('    </color-palette>', file=f)

		print("    </preferences>", file=f)
		print("</workbook>", file=f)

if __name__ == "__main__":
	#Change cmap_range as required from 0 to 1.
	cmap_range = (0.15, 0.85)
	create_cmasher_tableau_properties_file(cmap_range)