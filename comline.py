from __future__ import print_function

import argparse
import os.path

class ComLine():
	'Class for implementing command line options'
	

	def __init__(self, args):
		parser = argparse.ArgumentParser()
		parser.add_argument("-m", "--popmap",
							dest='popmap',
							default="map.txt",
							help="Specify a tab-delimited population map (sample -> population)"
		)
		parser.add_argument("-p", "--phylip",
							dest='phy',
							default="input.phy",
							help="Specify a phylip file for input."
		)
		
		#check if files exist

		self.args = parser.parse_args()

		self.exists( self.args.popmap )
		self.exists( self.args.phy )

		print( self.args.popmap )
		print( self.args.phy )


	def exists(self, filename):
		if( os.path.isfile(filename) != True ):
			print( filename, "does not exist" )
			print( "Exiting program..." )
			print( "" );
			raise SystemExit