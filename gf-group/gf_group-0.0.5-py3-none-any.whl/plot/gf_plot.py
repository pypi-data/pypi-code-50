from plotly import graph_objs as go
from plotly.offline import plot, iplot
import plotly.graph_objs as go


def plot_timeseries(date_rng, data):
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=date_rng, y=data, name="T",
                         line_color='deepskyblue'))
	# fig.add_trace(go.Scatter(x=df.Date, y=df['AAPL.Low'], name="AAPL Low",
	#                          line_color='dimgray'))

	fig.update_layout(title_text='Time Series with Rangeslider',
                  xaxis_rangeslider_visible=True)
	fig.show()