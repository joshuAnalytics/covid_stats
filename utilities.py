import altair as alt
import pandas as pd 

def bar_chart(df,x,y,n):
    plot_data = df[y].sort_values(ascending=False).head(n)
    plot_data = plot_data.reset_index()[[x,y]]
    chart = alt.Chart(plot_data).mark_bar().encode(
        alt.X(x, sort=alt.EncodingSortField(field="country", op="count", order='ascending')),
        alt.Y(y)
    ).properties(width=400,height=250,title=f"{y} by {x} (top {n})")
    chart.configure_title(
        fontSize=20,
        font='Courier',
        anchor='start',
        color='gray'
    )
    return chart

def scatter_plot(df,x,y,z,n):
    plot = df.iloc[0:n]
    plot.reset_index(inplace=True)
    
    points = alt.Chart(plot).mark_point().encode(
    x=x + ":Q",
    y=y + ":Q"
).properties(width=450,height=450,title=f"{y} vs {x}")

    text = points.mark_text(
        align='left',
        baseline='middle',
        dx=7
    ).encode(
        text=z
    )

    return points + text
