from pyffmpeg import FFmpeg

inp = 'C:\\Users\\gregory.morel\\Downloads\\VIDEO-2020-11-22-09-18-381.mp4'
out = 'C:\\Users\\gregory.morel\\Downloads\\VIDEO-2020-11-22-09-18-381.mp3'

ff = FFmpeg()

output_file = ff.convert(inp, out)

print(output_file)