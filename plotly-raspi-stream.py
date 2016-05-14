import plotly.plotly as py
from plotly.graph_objs import Scatter, Layout, Figure
import time
import readadc

username = 'toanbeokt'
api_key = 'wi8sa6o7cs'
stream_token = '2vetdxljbx'

py.sign_in(username, api_key)

trace1 = Scatter(
    x=[],
    y=[],
    stream=dict(
        token=stream_token,
        maxpoints=200
    )
)

layout = Layout(
    title='Raspberry Pi Streaming Sensor Data'
)

fig = Figure(data=[trace1], layout=layout)

print py.plot(fig, filename='Raspberry Pi Streaming Example Values')

# temperature sensor connected channel 0 of mcp3008
audio_level=0

stream = py.Stream(stream_token)s
stream.open()

#the main sensor reading loop
while True:
        sensor_data = readadc.readadc(sensor_pin, readadc.PINS.SPICLK, readadc.PINS.SPIMOSI, readadc.PINS.SPIMISO, readadc.PINS.SPICS)
        stream.write({'x': i, 'y': sensor_data})
        i += 1
        # delay between stream posts
        time.sleep(0.25)
