# Purpose: This is a class that encapsulates the ffmpeg-tools config file and its properties

import ConfigParser

class ConfigReader:

	def __init__(self):
		config = ConfigParser.RawConfigParser()
		config.read('../resources/config.ini')

		self.ffmpegCmd = config.get('ffmpeg properties', 'ffmpeg_command')
		self.resourcesDir = config.get('global properties', 'resources_dir')
		self.fontsDir = config.get('global properties', 'fonts_dir')
		self.inputDir = config.get('global properties', 'input_dir')
		self.outputDir = config.get('global properties', 'output_dir')