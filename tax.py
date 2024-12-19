import tax_Base
import plotly.graph_objects as go
import numpy as np

# Example usage:
#Input
severance_pay = 215000  # Severance pay received

f = lambda x: tax_Base.calc_tax1(x, severance_pay)
g = lambda x: tax_Base.calc_sevonly1(x, severance_pay)
h = lambda x: tax_Base.calc_netIncome1(x, severance_pay)

net = lambda x: tax_Base.calc_netCent1(x, severance_pay)


x = np.linspace(20000, 120000, 50)


fig = go.Figure()

fig.add_trace(
    go.Scatter(x=x, y=f(x),
               name = 'tax')
)

fig.add_trace(
    go.Scatter(x=x, y=g(x),
               name = 'taxSevOnly')
)

fig.add_trace(
    go.Scatter(x=x, y=h(x),
               name = 'netIncome')
)
fig.show()



fig = go.Figure()

fig.add_trace(
    go.Scatter(x=x, y=net(x),
               name = 'netCent')
)

fig.show()

fig = go.Figure()

fig.add_trace(
    go.Scatter(x=x, y=h(x),
               name = 'netIncome')
)

fig.show()


